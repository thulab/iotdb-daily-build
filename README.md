# title

| 版本   | 打包项                                                                                   |
|------|---------------------------------------------------------------------------------------|
| 0.12 | all, server, cli, grafana-connector, client-cpp                                       |
| 0.13 | all, server, cli, grafana-connector, grafana-plugin, client-cpp                       |
| 0.14 | all, server, cli, grafana-connector, grafana-plugin, datanode, confignode, client-cpp |



| iotdb             | 0.11 | 0.12 | 0.13 | 0,14 |
|-------------------|------|------|------|------|
| all               |
| server            |
| cli               |
| grafana-connector |
| grafana-plugin    |
| client-cpp        |
| python            |
| spark             |
| hadoop            |

| iotdb-benchmark |
|-----------------|
| 0.11            |
| 0.12            |
| 0.13            |
| 0.14            |
| influxdb        |
| kairosdb        |
| timescaledb     |
| taosd           |

## 当前打包内容
当前计划，分成3个
1. 主
   1. 打包all，server，这些
2. windows打包client-cpp
   1. 只打包windwos相关内容，当前只有client-cpp-win
   2. 为了提速
      1. 把mvn缓存拿过来用
      2. 新建个仓库，寸一份打包完成的boost
3. benchmark
   1. 打包各个benchmark的包

## tips
### push到另外一个仓库
参考https://github.com/marketplace/actions/push-directory-to-another-repository，
```shell
Generate your personal token following the steps:

Go to the GitHub Settings (on the right-hand side on the profile picture)
On the left-hand side pane click on "Developer Settings"
Click on "Personal Access Tokens" (also available at https://github.com/settings/tokens)
Generate a new token, choose "Repo". Copy the token.
Then make the token available to the Github Action following the steps:

Go to the GitHub page for the repository that you push from. Click on "Settings"
On the left-hand side pane click on "Secrets" then "Actions"
Click on "New repository secret"
Name: "API_TOKEN_GITHUB"
Value: paste the token that you copied earlier
```