# KubeSky.py

Send Kubernetes Events to Skype group

## Install and Run

```bash
# install dependency
pip3 install kubernetes skpy --user

# install app
cp kubesky.py $USER/.local/bin/kubesky.py
chmod +x $USER/.local/bin/kubesky.py

# install systemd services
mkdir -p $USER/.config/systemd/user
cp kubesky.service $USER/.config/systemd/user

# start
systemctl --user enable kubesky.service --now
```
