import matplotlib.pyplot as plt

from SimPEG.FLOW import Richards
from SimPEG import Mesh

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
mesh = Mesh.TensorMesh([10])
VGparams = Richards.Empirical.VanGenuchtenParams()
leg = []
these = ['sand', 'loam', 'sandy_clay', 'clay']
for p in these:
    if p[0] == '_' or p not in these:
        continue
    soil_name = p.replace('_', ' ')
    soil_name = soil_name[0].upper() + soil_name[1:]
    leg += [soil_name]
    params = getattr(VGparams, p)
    k_fun, theta_fun = Richards.Empirical.van_genuchten(mesh, **params)
    theta_fun.plot(ax=axes[0])
    k_fun.plot(ax=axes[1])

plt.tight_layout()
plt.legend(leg, loc=3)
axes[0].set_ylabel('Hydraulic conductivity, $k$')
axes[0].set_xlabel('Pressure head, $-\psi$')
axes[1].set_xlabel('Pressure head, $-\psi$')

fig.savefig('van-genuchten.png', dpi=200)
