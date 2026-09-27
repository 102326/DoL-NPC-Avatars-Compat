# NPC Avatars Mod 1.4.1-dol05119.1

基于 [Eudemonism00](https://github.com/Eudemonism00) 的 [NPC Avatars Mod](https://github.com/Eudemonism00/DOL-NPC-Avatars-Mod) 1.4.1 制作。感谢原作者提供代码和全部头像素材；这是第三方兼容修订，不是原作者的官方发布。

目标：DoL 0.5.11.9 / ModLoader 2.101.1。

- 修复 Robin 受伤表情错误回落到普通头像。
- 修复 Great Hawk 特殊战利品状态缺图，回退到已有关系表情。
- 修复未安装 BeautySelector 时的错误提示。
- 保留全部 518 张原图片、原名、原功能挂载与作者说明。

下载 `.mod.zip` 后替换同名旧模组，不要同时启用两份。使用 BeautySelector 时确认 `converted-NPC Avatars Mod` 已启用，并完整重载。回退可重新导入原作者 1.4.1 包。

依赖：TweeReplacer >=1.0.0、ImageLoaderHook ^2.3.0；无需 Simple Frameworks。

隔离桌面原生加载器验证：19 个头像解码用例和三种提示状态通过。Android 真机、真实存档及完整第三方组合未验收；未实装 Sydney 拟态分支缺图及游戏基线间歇 skybox 错误详见仓库验证报告。

SHA256：`511e239bda29367f89d292dbf8261bacc26bc7fb364396abe4e2e99f0e67f8ab`

图像说明：您已使用NPC头像增添模组。游戏作者并未提供各位角色的具体形象，头像为模组二次创作，仅供爱好者交流，请勿将其当作官方形象。

原包允许在 DoL 相关范围内二改二转，并要求保留图像说明；本修订保留该条件和原作者署名。
