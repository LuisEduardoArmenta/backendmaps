# 🔗 Guía de Integración Frontend (Angular) + Backend (Django)

Esta guía te mostrará cómo conectar tu aplicación Angular con el backend Django.

---

## 🎯 Objetivo

Conectar el sidebar de Angular con la API de Django para:
- Guardar marcadores en la base de datos MySQL
- Sincronizar marcadores entre todos los dispositivos
- Persistir datos permanentemente

---

## 🚀 Paso 1: Asegurar que el Backend Esté Corriendo

### 1.1. Configurar MySQL

Edita `backend/maps_backend/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tu_base_de_datos',       # Tu nombre de BD
        'USER': 'tu_usuario',             # Tu usuario
        'PASSWORD': 'tu_contraseña',      # Tu contraseña
        'HOST': 'srv1234.hostinger.com',  # Tu host
        'PORT': '3306',
    }
}
```

### 1.2. Ejecutar Migraciones

```bash
cd backend
.\venv\Scripts\Activate.ps1
python manage.py migrate
```

### 1.3. Crear Superusuario (Opcional)

```bash
python manage.py createsuperuser
```

### 1.4. Ejecutar Servidor

```bash
python manage.py runserver
```

Verifica que funcione: **http://127.0.0.1:8000/api/markers/**

---

## 📝 Paso 2: Modificar el Servicio en Angular

### 2.1. Actualizar `ubicaciones.service.ts`

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

export interface UbicacionInfo {
  id: number;
  lat: number;
  lng: number;
  nombre: string;
  categoria: string;
  direccion: string;
  mostrarInfo?: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class UbicacionesService {
  private API_URL = 'http://127.0.0.1:8000/api/markers/';
  
  private ubicacionesSubject = new BehaviorSubject<UbicacionInfo[]>([]);
  public ubicaciones$ = this.ubicacionesSubject.asObservable();
  
  private ubicacionSeleccionadaSubject = new BehaviorSubject<google.maps.LatLngLiteral | null>(null);
  public ubicacionSeleccionada$ = this.ubicacionSeleccionadaSubject.asObservable();

  constructor(private http: HttpClient) {
    this.cargarUbicaciones();
  }

  /**
   * Carga ubicaciones desde el backend
   */
  cargarUbicaciones(): void {
    this.http.get<any>(this.API_URL).subscribe({
      next: (response) => {
        const ubicaciones = response.results.map((item: any) => ({
          id: item.id,
          nombre: item.nombre,
          categoria: item.categoria,
          direccion: item.direccion,
          lat: parseFloat(item.lat),
          lng: parseFloat(item.lng),
          mostrarInfo: false
        }));
        this.ubicacionesSubject.next(ubicaciones);
      },
      error: (error) => {
        console.error('Error al cargar ubicaciones:', error);
      }
    });
  }

  /**
   * Agrega una nueva ubicación al backend
   */
  agregarUbicacion(ubicacion: Omit<UbicacionInfo, 'id'>): void {
    const data = {
      nombre: ubicacion.nombre,
      categoria: ubicacion.categoria,
      direccion: ubicacion.direccion,
      lat: ubicacion.lat,
      lng: ubicacion.lng
    };

    this.http.post<any>(this.API_URL, data).subscribe({
      next: (response) => {
        console.log('✅ Ubicación guardada en el backend:', response);
        this.cargarUbicaciones(); // Recargar lista
      },
      error: (error) => {
        console.error('❌ Error al guardar ubicación:', error);
      }
    });
  }

  /**
   * Elimina una ubicación del backend
   */
  eliminarUbicacion(id: number): void {
    this.http.delete(`${this.API_URL}${id}/`).subscribe({
      next: (response) => {
        console.log('🗑️ Ubicación eliminada:', response);
        this.cargarUbicaciones(); // Recargar lista
      },
      error: (error) => {
        console.error('❌ Error al eliminar ubicación:', error);
      }
    });
  }

  /**
   * Actualiza una ubicación existente
   */
  actualizarUbicacion(id: number, datos: Partial<UbicacionInfo>): void {
    this.http.patch(`${this.API_URL}${id}/`, datos).subscribe({
      next: (response) => {
        console.log('✏️ Ubicación actualizada:', response);
        this.cargarUbicaciones(); // Recargar lista
      },
      error: (error) => {
        console.error('❌ Error al actualizar ubicación:', error);
      }
    });
  }

  /**
   * Limpia todas las ubicaciones
   */
  limpiarUbicaciones(): void {
    this.http.delete(`${this.API_URL}delete_all/`).subscribe({
      next: (response) => {
        console.log('🧹 Todas las ubicaciones eliminadas:', response);
        this.ubicacionesSubject.next([]);
      },
      error: (error) => {
        console.error('❌ Error al limpiar ubicaciones:', error);
      }
    });
  }

  /**
   * Establece la ubicación seleccionada en el mapa
   */
  setUbicacionSeleccionada(coords: google.maps.LatLngLiteral | null): void {
    this.ubicacionSeleccionadaSubject.next(coords);
  }

  /**
   * Toggle info window
   */
  toggleInfoWindow(id: number): void {
    const ubicacionesActuales = this.ubicacionesSubject.value;
    const ubicacionesActualizadas = ubicacionesActuales.map(u => ({
      ...u,
      mostrarInfo: u.id === id ? !u.mostrarInfo : false
    }));
    this.ubicacionesSubject.next(ubicacionesActualizadas);
  }
}
```

### 2.2. Importar HttpClientModule

En `app.config.ts`:

```typescript
import { ApplicationConfig, provideBrowserGlobalErrorListeners, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';  // ⬅️ AGREGAR

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideHttpClient(),  // ⬅️ AGREGAR
  ]
};
```

---

## 🧪 Paso 3: Probar la Integración

### 3.1. Ejecutar Ambos Servidores

**Terminal 1 - Backend:**
```bash
cd backend
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

**Terminal 2 - Frontend:**
```bash
cd project
ng serve
```

### 3.2. Abrir la Aplicación

```
http://localhost:4200
```

### 3.3. Probar Funcionalidad

1. Haz clic en el mapa
2. Completa el formulario
3. Haz clic en "Agregar"
4. Verifica en el backend: `http://127.0.0.1:8000/admin/`

---

## 📊 Flujo de Datos Completo

```
Angular Frontend (Puerto 4200)
         ↓
    HTTP Request
         ↓
Django Backend (Puerto 8000)
         ↓
    MySQL Database (Nube)
         ↓
    HTTP Response
         ↓
Angular Frontend (Actualiza UI)
```

---

## 🔍 Debugging

### Ver Requests en la Consola

En el navegador (F12), pestaña "Network":
- Verás todas las peticiones HTTP
- Status 200 = OK
- Status 201 = Creado
- Status 400 = Error de validación
- Status 500 = Error del servidor

### Ver Logs del Backend

En la terminal donde corre `runserver`:
```
[15/Jan/2024 10:30:00] "POST /api/markers/ HTTP/1.1" 201 234
[15/Jan/2024 10:30:05] "GET /api/markers/ HTTP/1.1" 200 1024
```

---

## 🛠️ Configuración Adicional

### Manejo de Errores en Angular

```typescript
agregarUbicacion(ubicacion: Omit<UbicacionInfo, 'id'>): void {
  const data = {
    nombre: ubicacion.nombre,
    categoria: ubicacion.categoria,
    direccion: ubicacion.direccion,
    lat: ubicacion.lat,
    lng: ubicacion.lng
  };

  this.http.post<any>(this.API_URL, data).subscribe({
    next: (response) => {
      console.log('✅ Ubicación guardada:', response);
      alert('Ubicación guardada exitosamente');
      this.cargarUbicaciones();
    },
    error: (error) => {
      console.error('❌ Error:', error);
      
      if (error.status === 400) {
        alert('Error de validación: ' + JSON.stringify(error.error));
      } else if (error.status === 500) {
        alert('Error del servidor. Verifica el backend.');
      } else {
        alert('Error de conexión. Verifica que el backend esté corriendo.');
      }
    }
  });
}
```

---

## 🌐 Para Producción

### 1. Backend en Hostinger

```python
# settings.py
ALLOWED_HOSTS = ['tu-dominio.com', 'api.tu-dominio.com']

CORS_ALLOWED_ORIGINS = [
    "https://tu-frontend.com",
]
```

### 2. Frontend Apuntando a Producción

```typescript
// environment.prod.ts
export const environment = {
  production: true,
  apiUrl: 'https://api.tu-dominio.com/api/markers/'
};

// ubicaciones.service.ts
import { environment } from '../../environments/environment';

export class UbicacionesService {
  private API_URL = environment.apiUrl;
  // ...
}
```

---

## ✅ Checklist de Integración

- [ ] Backend corriendo en puerto 8000
- [ ] Frontend corriendo en puerto 4200
- [ ] HttpClientModule importado en Angular
- [ ] UbicacionesService actualizado con HttpClient
- [ ] CORS configurado en Django
- [ ] MySQL configurado y migraciones ejecutadas
- [ ] Crear marcador desde Angular → Se guarda en MySQL
- [ ] Recargar página → Los marcadores persisten
- [ ] Eliminar marcador → Se elimina de MySQL

---

## 🎉 ¡Listo!

Ahora tienes un sistema completo:
- Frontend Angular con mapa interactivo
- Backend Django con API REST
- Base de datos MySQL para persistencia
- Sincronización en tiempo real

**¡Tu aplicación de mapas está completa y funcional!** 🗺️✨

