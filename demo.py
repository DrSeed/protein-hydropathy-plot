import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
kd={"A":1.8,"R":-4.5,"N":-3.5,"D":-3.5,"C":2.5,"Q":-3.5,"E":-3.5,"G":-0.4,"H":-3.2,"I":4.5,
"L":3.8,"K":-3.9,"M":1.9,"F":2.8,"P":-1.6,"S":-0.8,"T":-0.7,"W":-0.9,"Y":-1.3,"V":4.2}
rng=np.random.default_rng(5);aa=list(kd)
seq=list(rng.choice(aa,300))
for s in (60,160):  # plant two hydrophobic (membrane-like) stretches
    for i in range(s,s+19):seq[i]=rng.choice(["I","L","V","F","M","A"])
vals=np.array([kd[a] for a in seq]);w=19
prof=np.convolve(vals,np.ones(w)/w,mode="valid")
plt.figure(figsize=(9,3.5));plt.plot(prof);plt.axhline(1.6,ls="--",c="r",label="TM threshold ~1.6")
plt.axhline(0,c="k",lw=.5);plt.xlabel("residue");plt.ylabel("hydropathy");plt.title("Kyte-Doolittle hydropathy (demo data)");plt.legend()
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"peaks above TM threshold: {int((prof>1.6).any())}\n");print("ok")