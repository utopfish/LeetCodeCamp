var foo = {
    name: 'vue',
    version: '2.0'
  }
  
  function observe(data) {
      if (!data || typeof data !== 'object') {
          return
      }
      // 使用递归劫持对象属性
      Object.keys(data).forEach(function(key) {
          defineReactive(data, key, data[key]);
      })
  }
  
  function defineReactive(obj, key, value) {
       // 监听子属性 比如这里data对象里的 'name' 或者 'version'
       observe(value)
  
      Object.defineProperty(obj, key, {
          get: function reactiveGetter() {
              return value
          },
          set: function reactiveSetter(newVal) {
              if (value === newVal) {
                  return
              } else {
                  value = newVal
                  console.log(`监听成功：${value} --> ${newVal}`)
              }
          }
      })
  }
  
  observe(foo)
  foo.name = 'angular' // “监听成功：vue --> angular”