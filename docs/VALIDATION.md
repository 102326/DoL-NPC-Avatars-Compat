# 验证记录与边界

目标：DoL 0.5.11.9 / ModLoader 2.101.1；日期：2026-09-27。

适配 ZIP SHA256：`511e239bda29367f89d292dbf8261bacc26bc7fb364396abe4e2e99f0e67f8ab`。
原包 SHA256：`f76a1eabeeed1107b3d2d6fb5b3a9f7a622735fa8824a4354ef0c6825a8d565f`。
只读游戏基线 SHA256：`3104933a6e5cd3c7876caa057556bd467e60c90460faddca62d1e36b6cbcabd6`。

## 通过

- manifest 声明文件全部存在，原 HTML 的四个替换锚点各唯一命中。
- 所有 518 张图片与原包逐字节相同；ZIP CRC、版本和重复构建哈希正常。
- 枚举 507 个图片路径：506 个存在，1 个原包未实装分支缺图明确列为限制。
- 在独立浏览器上下文中，以原生 ModLoader 加载 ZIP，Start → Start2 和社交挂载正常。
- Robin 男女各 hurt=0/1/2，共 6 个用例，正确选择 default/conflicted/betrayed 并实际解码 PNG。
- Great Hawk dom=0/50 × rocks/lurker_for_children/food，共 6 个用例，正确回退或保留专用头像并实际解码。
- Robin/Kylar/Eden × haunt/despair，共 6 个拟态用例实际解码成功。
- 第 19 个用例重新渲染 Robin 受伤分支，待渐入完成后截图并人工查看。
- BSA 缺席、已启用、未启用三种受控 API 状态的说明文字符合预期。

## 原包复现与已知限制

原包在 Robin hurt=1/2 时仍显示 default 图；修订后同场景通过。Great Hawk 原逻辑可能构造不存在的 rocks/children 图片路径，修订后采用现有关系表情。

原包 Sydney 拟态的非 haunt、草莓金发组合引用 `syd_iwb_st.png`，素材不存在。当前原版只设置 Robin/Kylar/Eden 拟态，所以保留这个未实现分支并明确记录，不扩展剧情或编造图片。如果第三方模组开启它，仍不保证支持。

隔离加载期间有时出现 `bannerFallbackImage.onload` 的 `Cannot read properties of undefined (reading 'skybox')`。无 NPC 模组控制组同样复现，属于已记录的间歇基线错误。不能宣称整合游戏“全程零错误”。

## 未验证

Android 真机、真实存档、全部 NPC 阈值与节日差分、Bedroom 海报交互、完整社交布局矩阵、无 BSA 的完整安装组合，以及 DoLSims/maplebirch/猫咖/Game UI/自定义 Loader Core 叠加组合。受控提示状态测试不等于三套完整安装组合。

运行验证使用隔离新游戏中的合成关系状态，没有使用用户存档。包含游戏内容的原始测试夹具、运行日志与机器路径留在本地，没有公开。仓库提供可独立运行的构建及资源枚举检查；上述游戏运行测试需要合法持有的相同游戏基线，不能仅靠本仓库重现。
