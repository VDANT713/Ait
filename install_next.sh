export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

npx -y create-next-app@latest next-app --typescript --tailwind --eslint --app --src-dir --import-alias "@/*" --use-npm

# Move all generated files to the current directory
mv next-app/* .
mv next-app/.* . 2>/dev/null || true
rm -rf next-app
