echo "Install Bazel build tool"
sudo wget -O /usr/local/bin/bazel https://github.com/bazelbuild/bazelisk/releases/latest/download/bazelisk-linux-$([ $(uname -m) = "aarch64" ] && echo "arm64" || echo "amd64")
sudo chmod +x /usr/local/bin/bazel
echo "Done!"

echo "Let's clone the repository..."
git clone https://github.com/envoyproxy/envoy.git
cd envoy
echo "Done!"

echo "Building envoy (brace yourselves)..."
bazel build -c opt envoy
echo "Done!"