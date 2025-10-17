# 🔧 Configurar MySQL Remoto en Hostinger

## 📌 Estado Actual

✅ **Tu backend está funcionando con SQLite** (base de datos local)  
⚠️ **MySQL remoto requiere configuración adicional en Hostinger**

---

## 🎯 Para Cambiar a MySQL

### Paso 1: Habilitar MySQL Remoto en Hostinger

1. **Inicia sesión en Hostinger**
2. **Ve a tu panel de control (hPanel)**
3. **Busca "Bases de datos" → "MySQL Remoto"**
4. **Habilita el acceso remoto a MySQL**

### Paso 2: Agregar tu IP a la Whitelist

En la sección de MySQL Remoto:

1. **Agrega tu IP pública actual**
   - Puedes obtenerla en: https://www.whatismyip.com/
   
2. **O permite todas las IPs** (solo para desarrollo):
   - Agrega: `%` (permite cualquier IP)

### Paso 3: Verificar el HOST Correcto

El HOST para conexiones remotas puede ser diferente. Verifica en Hostinger:

- **HOST Local (phpMyAdmin):** `localhost` o `127.0.0.1`
- **HOST Remoto:** Puede ser algo como:
  - `auth-db1026.hstgr.io`
  - `mysql.hostinger.com`
  - Tu IP del servidor
  - Depende de tu plan

### Paso 4: Actualizar `settings.py`

Una vez habilitado MySQL remoto, edita `backend/maps_backend/settings.py`:

**Comenta la configuración de SQLite:**
```python
# 🟢 SQLite para desarrollo local (INACTIVO)
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
```

**Descomenta la configuración de MySQL:**
```python
# Configuración para MySQL en la nube (ACTIVO)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u739395885_map',
        'USER': 'u739395885_ltx',
        'PASSWORD': 'mF5vpmgmv7bfVrM.19',
        'HOST': 'auth-db1026.hstgr.io',  # Verifica este HOST
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'auth_plugin': 'mysql_native_password',
        },
    }
}
```

### Paso 5: Ejecutar Migraciones en MySQL

```bash
python manage.py migrate
```

---

## 🔍 Verificar Configuración de Hostinger

### Dónde Encontrar las Credenciales Correctas:

1. **Panel de Hostinger**
2. **Bases de datos**
3. **Tu base de datos: `u739395885_map`**
4. **Verás:**
   - Nombre de la base: `u739395885_map` ✅
   - Usuario: `u739395885_ltx` ✅
   - Contraseña: `mF5vpmgmv7bfVrM.19` ✅
   - Servidor (HOST): **Esto es lo que necesitas verificar** ⚠️

### HOST Puede Ser:

- `localhost` (solo funciona dentro del servidor)
- `auth-db1026.hstgr.io` (para conexiones remotas)
- `mysql.hostinger.com`
- Una IP específica
- **Depende de tu plan de Hostinger**

---

## ❌ Errores Comunes

### Error 1045: Access Denied

```
django.db.utils.OperationalError: (1045, "Access denied...")
```

**Causas:**
- MySQL Remoto no está habilitado
- Tu IP no está en la whitelist
- Contraseña incorrecta
- HOST incorrecto

**Solución:**
1. Habilita MySQL Remoto en Hostinger
2. Agrega tu IP a la whitelist
3. Verifica el HOST correcto

### Error 2059: Authentication Plugin

```
MySQLdb.OperationalError: (2059, <NULL>)
```

**Causa:**
- Plugin de autenticación no compatible

**Solución:**
- Ya está configurado en `OPTIONS`:
  ```python
  'auth_plugin': 'mysql_native_password'
  ```

### Error 2003: Can't Connect

```
MySQLdb.OperationalError: (2003, "Can't connect to MySQL server...")
```

**Causas:**
- HOST incorrecto
- Puerto bloqueado
- Firewall bloqueando la conexión

**Solución:**
- Verifica el HOST correcto en Hostinger
- Verifica que el puerto 3306 esté abierto
- Contacta soporte de Hostinger si persiste

---

## 🌐 Alternativa: Usar SQLite y Migrar Después

### Ventajas de SQLite para Desarrollo:

✅ No requiere configuración  
✅ Funciona inmediatamente  
✅ Perfecto para desarrollo local  
✅ Fácil de compartir (un solo archivo)  

### Cuándo Cambiar a MySQL:

- Cuando despliegues a producción
- Cuando necesites acceso desde múltiples dispositivos
- Cuando necesites funcionalidades específicas de MySQL

### Migrar Datos de SQLite a MySQL:

1. **Exportar datos de SQLite:**
   ```bash
   python manage.py dumpdata > data.json
   ```

2. **Cambiar a MySQL en `settings.py`**

3. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   ```

4. **Importar datos:**
   ```bash
   python manage.py loaddata data.json
   ```

---

## 📱 Contactar Soporte de Hostinger

Si sigues teniendo problemas:

1. **Chat en vivo de Hostinger**
2. **Pregunta específica:**
   > "Necesito habilitar acceso remoto a MySQL para mi base de datos `u739395885_map`. ¿Cuál es el HOST correcto para conexiones remotas y cómo agrego mi IP a la whitelist?"

---

## ✅ Estado Actual del Proyecto

### 🟢 Funcionando Ahora:

- ✅ Backend Django corriendo
- ✅ API REST funcional
- ✅ Base de datos SQLite activa
- ✅ Puedes crear, listar, editar, eliminar marcadores
- ✅ Frontend puede conectarse a la API

### ⚠️ Para Producción:

- [ ] Habilitar MySQL Remoto en Hostinger
- [ ] Configurar HOST correcto
- [ ] Agregar IP a whitelist
- [ ] Migrar a MySQL
- [ ] Configurar CORS específico (no `*`)
- [ ] Cambiar `DEBUG = False`
- [ ] Configurar `ALLOWED_HOSTS` específico

---

## 🚀 Siguiente Paso

**Ahora puedes usar tu backend localmente:**

```bash
# Backend corriendo en:
http://127.0.0.1:8000/api/markers/

# Panel admin:
http://127.0.0.1:8000/admin/
```

**Para crear un superusuario:**

```bash
python manage.py createsuperuser
```

---

## 📖 Documentación de Hostinger

- [Acceso Remoto a MySQL](https://support.hostinger.com/es/articles/1583245-como-acceder-a-mysql-de-forma-remota)
- [Gestión de Bases de Datos](https://support.hostinger.com/es/categories/1583223-bases-de-datos)

---

**Tu backend está funcionando! 🎉**

Puedes desarrollar con SQLite y cambiar a MySQL cuando lo necesites.

