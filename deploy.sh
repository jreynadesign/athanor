#!/usr/bin/env sh
# Publish the site to Cloudflare Pages (project "justinreyna"), same shape as
# avaganza / LINDERO. Not the live host yet: justinreyna.design is still served
# by GitHub Pages from main until the nameservers move to Cloudflare.
#
#   ./deploy.sh            production  -> justinreyna.pages.dev (and the domain, once attached)
#   ./deploy.sh preview    preview url -> <hash>.justinreyna.pages.dev, for review before going live
#
# Stages from `git archive HEAD`, so only committed files can ship: the trial
# fonts, STYLE.md, DIRECTION.md and anything uncommitted never leave this Mac.
set -e
cd "$(dirname "$0")"

python3 build.py
if [ -n "$(git status --porcelain -- index.html 404.html work experiments sitemap.xml)" ]; then
  echo "deploy: build.py changed generated pages that aren't committed. commit them first."
  exit 1
fi

BRANCH=main
[ "$1" = "preview" ] && BRANCH=preview

STAGE=out/stage
rm -rf "$STAGE" && mkdir -p "$STAGE"
git archive HEAD | tar -x -C "$STAGE"
# repo-only files: sources, tooling, docs
rm -rf "$STAGE/build.py" "$STAGE/deploy.sh" "$STAGE/tools" "$STAGE/README.md" "$STAGE/.gitignore" "$STAGE/CNAME"
echo "staged $(find "$STAGE" -type f | wc -l | tr -d ' ') files ($(du -sh "$STAGE" | cut -f1))"
npx --yes wrangler@latest pages deploy "$STAGE" --project-name=justinreyna --branch="$BRANCH" --commit-dirty=true
