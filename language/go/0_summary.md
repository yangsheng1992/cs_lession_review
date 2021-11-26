1. go_module

        go mod init  # 初始化 go.mod
        go mod tidy  # 更新依赖文件
        go mod download  # 下载依赖文件
        
        go mod vendor  # 将依赖转移至本地的 vendor 文件
        go mod edit  # 手动修改依赖文件
        go mod graph  # 打印依赖图
        go mod verify  # 校验依赖

2. go_path
        
        1. 全局go_path
        2. 项目go_path {
            src：存放源代码
            pkg：编译后生成的文件
            bin：编译后生成的可执行文件
        }
        

3. 代码组织结果

        GOPATH下的src目录就是接下来开发程序的主要目录，所有的源码都是放在这个目录下面，那么一般我们的
        做法就是一个目录一个项目，例如: $GOPATH/src/mymath 表示mymath这个应用包或者可执行应用，
        这个根据package是main还是其他来决定，main的话就是可执行应用，其他的话就是应用包，这个会在后续
        详细介绍package。

4. go命令

    ```markdown
        1. go build 
        2. go clean 这个命令是用来移除当前源码包和关联源码包里面编译生成的文件
            -i 清除关联的安装的包和可运行文件，也就是通过go install安装的文件
            -n 把需要执行的清除命令打印出来，但是不执行，这样就可以很容易的知道底层是如何运行的
            -r 循环的清除在import中引入的包
            -x 打印出来执行的详细命令，其实就是-n打印的执行版本
        3. go fmt 格式化代码风格 gofmt -w -l src
        4. go get
        5. go install 第一步是生成结果文件(可执行文件或者.a包)，第二步会把编译好的结果移到$GOPATH/pkg或者$GOPATH/bin。
        6. go test 测试框架
        7. go tool 很多工具 
        8. godoc
    ```