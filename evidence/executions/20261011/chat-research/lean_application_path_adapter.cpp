// Container adapter for Lean IO.appPath: only this process executable path.
// No Lean parser, elaborator, tactic, proof term, or kernel code is replaced.
#include <cstdlib>
#include <cstring>
#include <cstddef>
#include <cstdio>
#include <unistd.h>
#include <sys/syscall.h>
extern "C" ssize_t readlink(const char* name, char* buffer, std::size_t size) {
    char current[64];
    std::snprintf(current,sizeof(current),"/proc/%d/exe",static_cast<int>(getpid()));
    const char* path=std::getenv("BGS_LEAN_APPLICATION_PATH");
    if (path && (!std::strcmp(name,current) || !std::strcmp(name,"/proc/self/exe"))) {
        const std::size_t n=std::strlen(path);
        const std::size_t count=n<size?n:size;
        std::memcpy(buffer,path,count);
        return static_cast<ssize_t>(count);
    }
    return static_cast<ssize_t>(syscall(SYS_readlink,name,buffer,size));
}
