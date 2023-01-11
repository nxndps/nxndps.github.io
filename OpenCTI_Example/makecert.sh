openssl req -new -x509 -newkey rsa:4096 -sha256 \
-keyout simplekey.pem -out simplecert.pem \
-days 30 -nodes -subj "/C=US/ST=TX/L=Austin/O=Dialpad/CN=local.test.dom" 
#\
#-addext "subjectAltName=DNS:local.test.dom,DNS:test.dom,IP:127.0.0.1"

# when using some browsers a self signed cert may cause issues.
# brave will allow you to bypass this by typing "thisisunsafe"
# when the warning appears. This is no enty field or other indication
# that you may do this but it is allowed.