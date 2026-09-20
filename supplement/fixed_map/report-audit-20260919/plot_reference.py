"""Plot an exact reference and a clearly labeled finite diagnostic."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

root = Path(__file__).parent
x = np.linspace(0,1.5,401)
X,Y = np.meshgrid(x,x)
H = 1-np.maximum(1-X,0)-np.maximum(1-Y,0)+np.maximum(1-X-Y,0)
fig, axes = plt.subplots(1,2,figsize=(10,4.4),layout='constrained')
im=axes[0].pcolormesh(X,Y,H,shading='auto',cmap='viridis',vmin=0,vmax=1,rasterized=True)
axes[0].plot([0,1],[1,0],'w--',lw=1.3)
axes[0].plot(.75,.75,'o',mfc='none',mec='white',ms=8)
axes[0].set(xlabel='a / N',ylabel='b / N',title='Exact CUE cubic reference',aspect='equal')
fig.colorbar(im,ax=axes[0],label='E[Tr U^a Tr U^b Tr U^(-a-b)] / N')
data=json.loads((root/'monodromy_experiment.json').read_text())
cal=json.loads((root/'cubic_variance.json').read_text())
rms=next(r['cue_root_mean_square_fluctuation'] for r in cal['finite_calibration'] if r['N']==1393)
axes[1].add_patch(Circle((.5,0),rms,fill=False,ec='#536477',ls='--',lw=1.5,
                        label='CUE RMS distance (not a confidence region)'))
axes[1].plot(.5,0,'k+',ms=11,mew=2,label='CUE mean')
for row,color in zip([r for r in data['rows'] if r['N']==1393],['#dd6b20','#2563a6']):
    re,imval=row['smoothed_cubic']
    axes[1].plot(re,imval,'o',color=color,ms=7,label=f"kappa = {row['kappa']}")
axes[1].axhline(0,color='#ccd2da',lw=.7,zorder=-1)
axes[1].set(xlabel='Real part',ylabel='Imaginary part',title='Redesigned kick: finite N = 1393',
            xlim=(-.08,1.08),ylim=(-.58,.9),aspect='equal')
axes[1].legend(loc='upper left',bbox_to_anchor=(-.02,-.16),frameon=False,fontsize=8)
fig.savefig(root/'cue_reference.png',dpi=180)
fig.savefig(root/'cue_reference.svg')
plt.close(fig)
print(root/'cue_reference.png')
