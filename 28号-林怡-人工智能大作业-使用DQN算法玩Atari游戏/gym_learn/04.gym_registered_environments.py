from gym import envs

print(envs.registry.all())  # 支持将自己环境添加到注册表中去,扩展性不错.不过我是用不着了
print("end")
