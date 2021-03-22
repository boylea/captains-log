prometheus_version="2.25.2"
release_name="prometheus-${prometheus_version}.linux-amd64"
download_url="https://github.com/prometheus/prometheus/releases/download/v${prometheus_version}/${release_name}.tar.gz"
dest="/tmp/${release_name}.tar.gz"

wget -O $dest $download_url
tar -xzf $dest
cp prometheus.template prometheus.yml
sed -i "s|__REMOTE_URL__|${REMOTE_URL}|g" prometheus.yml
sed -i "s|__BEARER_TOKEN__|${BEARER_TOKEN}|g" prometheus.yml
./${release_name}/prometheus --config.file=prometheus.yml &