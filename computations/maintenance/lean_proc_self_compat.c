/* Optional Linux compatibility shim for runtimes exposing /proc/self/exe
 * but not /proc/<getpid()>/exe. Lean 4.33.1 uses the latter to find its
 * installation. Only that exact self lookup is redirected; all other
 * readlink calls are delegated unchanged. No Lean proof code is modified.
 *
 * cc -shared -fPIC -O2 lean_proc_self_compat.c -ldl -o compat.so
 * LD_PRELOAD=/absolute/path/compat.so /absolute/path/to/lean --version
 */
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

ssize_t readlink(const char *path, char *buffer, size_t size) {
    typedef ssize_t (*readlink_fn)(const char *, char *, size_t);
    readlink_fn original;
    void *symbol = dlsym(RTLD_NEXT, "readlink");
    _Static_assert(sizeof original == sizeof symbol, "POSIX function pointer size");
    memcpy(&original, &symbol, sizeof original);
    if (!original) { errno = ENOSYS; return -1; }
    char own_path[64];
    snprintf(own_path, sizeof own_path, "/proc/%ld/exe", (long)getpid());
    if (strcmp(path, own_path) == 0) path = "/proc/self/exe";
    return original(path, buffer, size);
}
