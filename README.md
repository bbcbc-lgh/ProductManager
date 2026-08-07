# Codex 产品协作系统使用说明

这是一套面向 Codex Desktop 的产品开发工作流模板。它用一个主 agent 从产品想法推进到发布，通过阶段文档保留上下文，通过独立审查和脚本门禁防止假完成。

## 1. 工作流总览

```text
产品想法
  -> REQUIRE.md              需求文档
  -> BRIEF.md                设计规范
  -> DESIGN/                 视觉方案与高保真原型，可选
  -> PLAN.md                 分阶段开发计划
  -> 代码、验证证据、独立审查
  -> 隐私审计、打包和发布
```

默认由一个主 agent 负责全流程。只有以下情况才派子 agent：

- 开发完成后的干净上下文独立审查；
- 自进化信号的干净上下文分析；
- 边界明确、可以真正并行且不会争用同一文件的工作。

## 2. 创建新产品项目

复制整个模板目录，并将副本改成产品名称。例如：

```powershell
Copy-Item -Recurse 'E:\Product-Manager' 'E:\Projects\my-product'
Set-Location 'E:\Projects\my-product'
git init
```

Git 不是工作流的硬依赖，但建议初始化。独立审查需要检查实际 diff，Git 可以显著提高审查可靠性。

随后在 Codex Desktop 中打开新项目根目录，并新建一个 task。首次使用时，Codex 可能要求信任项目内 `.codex/hooks.json`，确认内容后允许它运行。该 hook 只负责检查尚未处理的自进化信号。

不要直接在本模板目录里开发具体产品；将它作为新项目的起点。

## 3. 从第一条消息开始

新项目中的第一条消息可以直接使用：

```text
我要从零开始创建一个产品。

初步想法：
[描述产品想法，不完整也可以]

请先使用 $goal-creator，把“完成需求收集并产出可直接开发的
REQUIRE.md”创建为可验证的 Goal，然后使用
$product-require-builder 采访我。

不要奉承，不要替我隐含地做产品决策。发现矛盾、伪需求、
范围过大或无法验收的描述时直接指出。阻塞问题解决前不要把
REQUIRE.md 标记为 ready。
```

主 agent 会从 `.codex/agents/templates/REQUIRE.md` 创建根目录的工作文档，并开始需求采访。

## 4. 六个产品阶段

### 4.1 需求收集

使用：`$goal-creator`、`$product-require-builder`

目标是把模糊想法逼问成根目录的 `REQUIRE.md`。合格文档至少需要明确：

- 问题、目标用户和使用场景；
- 核心流程、范围内功能和明确不做的内容；
- 数据、权限、业务规则和非功能要求；
- 优先级、风险和可观察的验收标准；
- `status: ready`，且没有未解决的阻塞问题。

需求不明确时继续回答问题，不要急着进入设计。

### 4.2 设计规范

使用：`$goal-creator`、`$product-design-brief-builder`

推荐提示词：

```text
请为“完成产品设计规范”创建 Goal，然后使用
$product-design-brief-builder 读取 REQUIRE.md 并采访我。
对于高级、简洁、专业等模糊感受，给出多个实质不同的设计方向，
让我选择后再转化为具体设计决策。最终产出 ready 状态的 BRIEF.md。
```

`BRIEF.md` 应明确色彩策略、明暗模式、信息密度、排版、字体角色、布局节奏、交互状态、动效、响应式行为、无障碍要求和禁止使用的设计模式。

### 4.3 视觉设计与高保真原型，可选

使用：`$goal-creator`、`$product-design-maker`

需要先验证视觉方案时发送：

```text
请为视觉设计创建 Goal，然后使用 $product-design-maker 读取
REQUIRE.md 和 BRIEF.md，产出完整的 DESIGN/ 设计方案和可检查的
高保真原型。
```

预期产物：

```text
DESIGN/
├─ DESIGN.md
├─ images/
└─ prototypes/
```

原型可以是 HTML/CSS、可运行的前端切片、图片或带注释的截图，只要核心流程和重要状态可以检查。

不需要这个阶段时明确发送：

```text
跳过可选的视觉设计阶段。后续 PLAN.md 记录本阶段已跳过，
以 REQUIRE.md 和 BRIEF.md 作为开发计划输入。
```

### 4.4 开发计划

使用：`$goal-creator`、`$product-dev-planner`

```text
请为开发计划创建 Goal，然后使用 $product-dev-planner 读取
REQUIRE.md、BRIEF.md，以及存在时的 DESIGN/。

把开发拆成能够独立运行、独立展示、独立验收的 Phase。
禁止产生写完后仍看不到效果的纯基础设施阶段。产出 ready 状态的 PLAN.md。
```

检查每个 Phase 是否都有：

- 一个具体、边界明确的结果；
- 可运行或可观察的演示方式；
- build、test 和 acceptance 验证方式；
- 明确依赖和验收标准；
- 独立代码审查要求。

### 4.5 分阶段开发

使用：`$goal-creator`、`$product-dev-builder`、`$code-reviewer`

一次只启动一个 Phase：

```text
请使用 $goal-creator 为 PLAN.md 的 Phase P01 创建并启动 Goal，
然后使用 $product-dev-builder 完成该 Phase。

采集 build、test、acceptance 证据；完成实现后派一个干净上下文的
独立子 agent，遵循 .codex/agents/code-reviewer.md 并使用
$code-reviewer 审查。持续修复到 verdict 为 PASS 且门禁通过，
再向我提交验收。
```

实现证据保存在：

```text
.codex/agents/evidence/<phase-id>/
├─ build.json
├─ test.json
└─ acceptance.json
```

独立审查保存在：

```text
.codex/agents/reviews/<phase-id>.yaml
```

手动检查门禁：

```powershell
python .codex\agents\scripts\workflow_gate.py --phase P01
```

只有输出包含以下结果时才进入下一 Phase：

```json
{
  "ok": true,
  "errors": []
}
```

### 4.6 发布

使用：`$goal-creator`、`$product-release-builder`

```text
请为发布创建 Goal，然后使用 $product-release-builder 检查当前项目。
先列出当前项目实际能够完成的所有发布类型，让我选择；不要提前发布。
选择后执行隐私、密钥、权限、遥测、第三方服务、依赖许可证、
构建复现、冒烟测试和回滚审计，再完成打包。
```

系统会根据项目实际情况列出 Web、桌面应用、移动应用、CLI、库或软件包、容器、静态产物等可行目标。列出目标不代表获得了对外发布权限；发布到生产环境或外部平台仍需用户明确授权。

## 5. Goal 的作用

每项实质工作先由 `$goal-creator` 写成可执行 Goal。一个合格 Goal 必须包括：

- 单一、明确的目标；
- 可验证的完成标准；
- 必须提交的验收证据；
- 精确的门禁命令；
- 明确的任务边界。

不要接受“完善产品”“把体验做好”“完成开发”这类无法验证的 Goal。Codex Desktop 提供 Goal 能力时，要求 agent 真正创建 Goal，而不是只在聊天中展示一段草稿。

## 6. 需求变更

开发中改变产品决定时，不要直接要求修改代码。使用：

```text
这是需求变更，不是普通代码修改：
[描述变化]

请分析它影响 REQUIRE.md、BRIEF.md、DESIGN/ 和 PLAN.md 中的哪些内容。
先更新上游文档并让我确认，再调整代码和受影响 Phase 的验收标准。
```

下游实现不能偷偷改写上游产品决定。否则跨阶段文档会失去约束作用。

## 7. 修复 Bug

使用 `$bug-fixer`：

```text
请使用 $bug-fixer 修复这个问题：
[复现方式、期望行为和实际行为]

先稳定复现并建立回归测试，再做最小修改。若修改影响共享行为，
完成后派独立子 agent 使用 $code-reviewer 审查。
```

没有复现证据、回归测试或明确环境阻塞时，不应宣称 Bug 已修复。

## 8. 自进化

当 Codex 的行为不符合你的习惯时，直接纠正它并明确要求记录信号：

```text
你这次一次问了太多问题。以后需求采访每轮只问最关键的少量问题。
把这次纠正记录为自进化信号，但现在不要直接修改规则。
```

信号保存在 `.codex/evolution/signals/`。下次新会话启动时，hook 会检测新信号，并要求主 agent 派一个干净上下文的进化分析子 agent。分析结果会逐条询问你是否接受；只有明确接受后，才允许修改 `AGENTS.md` 或 skill。

完整制度见 `.codex/EVOLUTION.md`。自进化应优先修改、合并或删除规则，而不是不断追加规则。

## 9. 创建或修改 Skill

本项目不提供同名的项目级 `skill-creator`。请使用 Codex 自带的 `$skill-creator`：

```text
请使用 Codex 内置的 $skill-creator，在 .agents/skills/ 下创建一个
名为 example-skill 的项目工作流 skill。
```

项目 skill 名称统一使用小写英文、数字和短横线。不要在 `.agents/skills/` 中重新创建 `skill-creator`，否则会与 Codex 内置 skill 冲突。

## 10. 关键目录

```text
项目根目录/
├─ .agents/
│  └─ skills/                    项目工作流 skill
├─ .codex/
│  ├─ agents/
│  │  ├─ schemas/                机器可检查的数据契约
│  │  ├─ scripts/                门禁、证据和信号脚本
│  │  ├─ templates/              阶段文档模板
│  │  ├─ evidence/               运行时生成的 Phase 证据
│  │  └─ reviews/                运行时生成的独立审查记录
│  ├─ evolution/
│  │  ├─ signals/                运行时生成的用户反馈信号
│  │  ├─ proposals/              运行时生成的规则修改提案
│  │  └─ state.json              自进化处理状态
│  ├─ hooks/
│  ├─ EVOLUTION.md
│  └─ hooks.json
├─ AGENTS.md                     项目工作流总约束
└─ README.md                     本使用说明
```

`REQUIRE.md`、`BRIEF.md`、`DESIGN/` 和 `PLAN.md` 会在对应阶段开始后出现在根目录，它们是产品开发产物，不是初始模板结构的一部分。

## 11. 常见问题

### Codex 没有自动使用某个 skill

在提示词中显式写出 `$skill-name`。复制模板后应新建 task，让 Codex 重新加载项目规则和 skill。

### hook 没有运行

确认项目已在 Codex Desktop 中被信任，并检查 `.codex/hooks.json` 是否处于已信任状态。hook 只在存在 `state: new` 的信号时向主 agent 注入自进化要求；没有新信号时它会保持静默。

### 门禁失败

直接阅读返回的 `errors`。常见原因包括文档仍为 `draft`、验收标准为空、尚有开放问题、缺少三类证据、审查文件缺失、`verdict` 不是 `PASS`，或仍有阻塞发现。

### 是否必须在一个 task 中完成全部产品

不必须。跨 task 上下文由 `REQUIRE.md`、`BRIEF.md`、`DESIGN/`、`PLAN.md`、Goal、证据和审查记录承接。新 task 开始时要求主 agent先读取这些文件，再继续当前 Phase。

### 是否可以跳过独立审查

开发 Phase 不可以。独立审查是阶段完成门禁的一部分。视觉设计阶段可以跳过，但必须在 `PLAN.md` 中明确记录。

## 12. 关闭会话前

建议确认：

- 当前阶段文档已经保存；
- 未决定事项写入 `open_questions`；
- 当前 Phase、Goal 状态和下一步清楚；
- build、test、acceptance 输出已采集；
- 用户纠正已经记录为信号；
- 没有把尚未通过门禁的工作写成已完成。

下一次打开项目后，可以发送：

```text
请读取 AGENTS.md、REQUIRE.md、BRIEF.md、存在时的 DESIGN/、PLAN.md，
以及当前 Goal、证据和审查记录。告诉我目前处于哪个 Phase、
有哪些阻塞项、下一项可执行动作是什么，然后继续工作。
```
