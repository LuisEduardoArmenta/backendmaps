# 🚀 Backend listo para Railway

## ✅ Todo configurado correctamente

Tu backend Django está completamente preparado para desplegar en Railway. Se crearon y configuraron los siguientes archivos:

### 📁 Archivos creados

1. **`Procfile`** - Define cómo iniciar la aplicación
2. **`railway.json`** - Configuración de build y deployment
3. **`runtime.txt`** - Especifica Python 3.12
4. **`requirements.txt`** - Actualizado con dependencias para producción
5. **`railway.env.example`** - Ejemplo de variables de entorno
6. **`verify_railway_config.py`** - Script de verificación (ya ejecutado ✅)

### ⚙️ Archivos modificados

- **`settings.py`** - Configurado para leer variables de entorno y usar PostgreSQL en Railway

---

## 🎯 Próximos pasos

### 1️⃣ Subir a GitHub

```bash
git add .
git commit -m "Backend configurado para Railway"
git push origin main
```

### 2️⃣ Crear proyecto en Railway

1. Ve a [railway.app](https://railway.app)
2. Login con GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecciona tu repositorio

### 3️⃣ Agregar PostgreSQL

1. En tu proyecto: "+ New" → "Database" → "PostgreSQL"
2. Railway conectará automáticamente `DATABASE_URL`

### 4️⃣ Configurar variables de entorno

En Railway → Variables, agrega:

| Variable | Valor recomendado |
|----------|-------------------|
| `SECRET_KEY` | `django-insecure-TU-CLAVE-SUPER-SEGURA-123` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*.railway.app` |

### 5️⃣ Deploy automático

Railway desplegará automáticamente en ~3 minutos. Verás tu URL:
```
https://tu-app-production.up.railway.app/api/markers/
```

---

## 🔗 Conectar con tu frontend Angular

Actualiza `frontend/project/src/app/services/ubicaciones.ts`:

```typescript
// Cambiar:
private apiUrl = 'http://127.0.0.1:8000/api/markers/';

// Por:
private apiUrl = 'https://tu-app-production.up.railway.app/api/markers/';
```

Y agrega la URL de tu frontend a Railway (Variables):
```
CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app
```

---

## 📚 Documentación completa

- **[RAILWAY_QUICKSTART.md](./RAILWAY_QUICKSTART.md)** - Guía rápida (5 min)
- **[RAILWAY_DEPLOY.md](./RAILWAY_DEPLOY.md)** - Guía detallada paso a paso
- **[RAILWAY_FILES.md](./RAILWAY_FILES.md)** - Explicación de cada archivo

---

## ✅ Verificación completada

El script `verify_railway_config.py` confirmó que:

- ✅ Todos los archivos obligatorios existen
- ✅ Todas las dependencias están en requirements.txt
- ✅ Procfile apunta correctamente a maps_backend.wsgi
- ✅ settings.py lee variables de entorno
- ✅ WhiteNoise está configurado
- ✅ .gitignore protege archivos sensibles

---

## 🎉 ¡Listo para deployment!

Railway hará automáticamente:

1. ✅ Instalar dependencias de requirements.txt
2. ✅ Ejecutar migraciones (`python manage.py migrate`)
3. ✅ Recopilar archivos estáticos (`collectstatic`)
4. ✅ Iniciar servidor con Gunicorn
5. ✅ Asignar HTTPS automáticamente

**Tu API estará disponible en:**
```
https://tu-app.railway.app/api/markers/
```

---

## 💡 Consejos

1. **Primera vez**: Usa el plan gratuito de Railway ($5/mes de crédito gratis)
2. **CORS**: Actualiza `CORS_ALLOWED_ORIGINS` cuando despliegues el frontend
3. **Secrets**: Nunca subas `.env` a GitHub (ya está en .gitignore)
4. **Logs**: Revisa los logs en Railway si algo falla
5. **Base de datos**: Los datos de SQLite local NO se migrarán (tendrás una BD vacía en Railway)

---

## 🆘 Si algo sale mal

1. Revisa los logs en Railway → Deployments
2. Verifica que PostgreSQL esté conectado
3. Confirma que las variables de entorno están configuradas
4. Asegúrate de que el dominio esté en `ALLOWED_HOSTS`

---

## 📞 Recursos

- [Documentación Railway](https://docs.railway.app/)
- [Django en Railway](https://docs.railway.app/guides/django)
- [Soporte Railway](https://railway.app/help)

---

**¡Tu backend Django está listo para la nube! 🚀**

