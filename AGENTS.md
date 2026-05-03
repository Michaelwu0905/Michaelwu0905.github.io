# Repository Guidelines

## Project Structure & Module Organization

This repository is a Hugo blog using the `reimu` theme. Site configuration starts in `hugo.toml`, with extra parameters in `config/_default/params.yml`. Blog posts live in `content/posts/`; use `archetypes/default.md` for new Markdown content. Static files copied as-is belong in `static/`, such as `static/images/` and `static/avatar/`. Generated output is written to `public/`. Theme source and custom assets are under `themes/reimu/`, including layouts, SCSS, TypeScript, translations, and vendored browser resources.

## Build, Test, and Development Commands

- `hugo server -D`: run the local development server and include draft content.
- `hugo`: build the production site into `public/`.
- `hugo --minify`: build minified production output.
- `cd themes/reimu && pnpm install`: install theme development tools if editing theme scripts or templates.
- `cd themes/reimu && pnpm commit`: create a conventional commit message with Commitizen.

Run Hugo commands from the repository root unless noted.

## Coding Style & Naming Conventions

Write posts in Markdown with clear front matter and lowercase, hyphenated filenames, for example `content/posts/my-new-post.md`. Keep Hugo templates in `layouts/` or `themes/reimu/layouts/` using Go template conventions. Theme styles are SCSS files in `themes/reimu/assets/css/`; prefer small partials for component-specific styles. Theme scripts are TypeScript in `themes/reimu/assets/js/`. The theme includes Prettier with `prettier-plugin-go-template`; use it for theme formatting.

## Testing Guidelines

There is no dedicated automated test suite. Validate changes by running `hugo` and fixing warnings or template errors before committing. For content changes, run `hugo server -D` and inspect affected posts, images, tags, and archive pages locally. For theme changes, check desktop and mobile layouts.

## Commit & Pull Request Guidelines

Recent commits use short Chinese summaries, often describing the completed change directly, such as `进行了主题的个性化配置`. The theme also provides Commitizen and commitlint with the conventional commit preset, so messages such as `fix: update post layout` are acceptable for theme work. Keep commits focused.

Pull requests should include a brief description, reason for the change, and screenshots for visual updates. Link related issues when available, and mention the validation command used, for example `hugo --minify`.

## Security & Configuration Tips

Do not commit secrets, analytics tokens, or private service credentials in `hugo.toml`, `config/_default/params.yml`, or workflow files. Keep generated `public/` changes separate from source changes unless the deployment process requires committing built output.
