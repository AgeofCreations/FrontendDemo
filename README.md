Шаг 1:
Создаёшь папки с frontend и backend в project_root

Шаг 2:
Из папки frontend выполняешь 
```bash
vue create <имя проекта>
```
Шаг 3: 
Создать в корне frontend файл vue.config.js с содержимым:

```
module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/public/'
    : './dev',
  outputDir: process.env.NODE_ENV === 'production'
    ? '../backend/static'
    : './dev'
}
// publicPath - путь к статическим файлам в URL.
// outputDir - путь, по которому npm билдит файлы в файловой системе
```
Шаг 4: написать вьюху, которая возвращает 
```web.Fileresponse("<Путь к index.html>")```
Шаг 5: Написать start_app
Шаг 6: добавить route, который будет вощвращать написанную вьюху и 
route, который будет содержать:
```
web.static("<URL статики>", "<Путь к статике в файловой системе>")
```

Готово. 
