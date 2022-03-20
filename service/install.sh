cp terramar.service /lib/systemd/system/terramar.service
chmod 644 /lib/systemd/system/terramar.service
systemctl daemon-reload
systemctl enable terramar.service
