fmt package

```go
func Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error) # 来格式化并输出到 io.Writers 而不是 os.Stdout
func Printf(format string, a ...interface{}) (n int, err error) # 输出对象为标准输出
func Sprintf(format string, a ...interface{}) string  # 格式化并返回一个字符串而不带任何输出， 可用于给其他函数传递格式化参数
func Errorf(format string, a ...interface{}) error
func Fprint(w io.Writer, a ...interface{}) (n int, err error) # 向io.Writer对象中输入字符，第一个参数为输入对象，后面的参数为字符串，直接输出
func Print(a ...interface{}) (n int, err error) # 属于标准输出流,一般使用它来进行屏幕输出, 是把输入对象默认为标准输出。
func Sprint(a ...interface{}) string #  是返回一个格式化的字符串
func Fprintln(w io.Writer, a ...interface{}) (n int, err error)
func Println(a ...interface{}) (n int, err error) # 输出后换行
func Sprintln(a ...interface{}) string
```

原生:
print 属于输出到标准错误流中并打印 


所有的函数名都是_print_格式的，其中_代表某个标志，标志及其含义如下：

| 标志 |	含义 |
| --- | --- |
| _f | 格式化|
|_ln|	换行|
|F_	|输入到某个对象|
|S_	|只返回而不做输出|

且，
fmt.Fprintf和fmt.Printf是一对
fmt.Fprint和fmt.Print是一对
fmt.Fprintln和fmt.Println是一对
不带F前缀的函数均是对带F前缀函数的调用，其输入对象均设置为标准输出

