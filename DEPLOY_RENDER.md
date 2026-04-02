# Render 部署说明（静态站点）

本项目是纯静态站点（HTML/CSS/JS），推荐使用 Render 的 **Static Site**。

## 1. 先改 `render.yaml`

编辑项目根目录的 `render.yaml`，把下面两项改成你的真实信息：

- `repo`: 你的 GitHub 仓库地址
- `branch`: 你要部署的分支（通常是 `main`）

当前文件位置：`/Users/liaowang/Desktop/NEED-56/render.yaml`

## 2. 推送到 GitHub

确保项目代码和 `render.yaml` 都已经推送到 GitHub。

## 3. 在 Render 创建服务

1. 打开 Render 控制台 -> **New +** -> **Blueprint**
2. 选择你的 GitHub 仓库
3. Render 会自动识别 `render.yaml` 并创建一个静态服务
4. 点击 **Apply** 或 **Create**

## 4. 关键配置检查（Render 页面）

创建后进入服务设置，确认：

- Service Type: `Static Site`
- Publish Directory: `.`
- Branch: 你的目标分支（如 `main`）
- Auto-Deploy: `On`

## 5. 访问与更新

- 首次部署完成后会得到一个 `onrender.com` 域名
- 后续每次 push 到对应分支，Render 会自动重新部署

## 可选：绑定自定义域名

在服务页 `Settings -> Custom Domains` 添加域名，并按提示配置 DNS。
