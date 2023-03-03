# tools 删除过早的tag (tools-delete_tags)
tools-delete_tags_step1.yml  
tools-delete_tags_step2.yml  
> ！！轻易的不要执行这两步

## 内容
该工作流由2个yml组成，step1和step2  

step1 执行之后，将只保留最新的20个tag，即清理10天以前的tag(1天2个)，被删除tag的release会变成"Draft"状态  
step2 执行之后，会删除10天以前且标记为"Draft"的release，但是一次只能删除30个，**如果过多需要多次多次执行该步骤**  

## 参考action
https://github.com/marketplace/actions/delete-draft-releases
