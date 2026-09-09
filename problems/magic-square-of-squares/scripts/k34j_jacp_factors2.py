print("Jac(P) factorization test: use the PARI gp from the local extraction")
print("(Sage's bundled gp had spawn issues; the standalone ~/pari gp works)")
import subprocess
GP = "/home/linux/pari/dl/ext/usr/bin/gp"
gpf = open("/home/linux/mss-k34/p_charpoly.gp").read()
out = subprocess.run([GP, "-q", "-f", "/home/linux/mss-k34/p_charpoly.gp"],
                     capture_output=True, text=True, timeout=560)
print(out.stdout)