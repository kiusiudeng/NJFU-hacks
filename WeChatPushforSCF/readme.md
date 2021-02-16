# 企业微信消息推送服务端

 腾讯云函数版。

## Tips

1. 在企业微信后台[创建一个APP](https://work.weixin.qq.com/wework_admin/frame#apps/createApiApp)，取得`AgentId`, `Secret`, `CorpID`，并填入源码。

2. 部署至[腾讯云函数](https://console.cloud.tencent.com/scf/index)。

3. 创建`API网关触发器`，获得`Callback URL`。参数格式如下：

   | 参数 | 必需   | 描述                                 |
   | :--: | ------ | ------------------------------------ |
   | text | **是** | 标题内容。                           |
   | desp | 否     | 正文内容。默认为“内容为空”           |
   | url  | 否     | 点击卡片跳转链接。默认为“http://url” |

   

