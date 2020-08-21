conf = "/etc/ssh/sshd_config"
fh = open(conf)

for line in fh:

    if line.startswith('#Port'):

        print(line)

fh.close()
