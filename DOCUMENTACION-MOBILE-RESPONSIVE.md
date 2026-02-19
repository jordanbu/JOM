# 📱 JOM - Documentación Completa Mobile Responsive

## 🎯 Visión General
JOM es una plataforma de reserva de hospedajes con diseño **100% responsive** que se adapta perfectamente de móviles a escritorio. Cada página está diseñada con un enfoque "mobile-first" usando Tailwind CSS, asegurando una experiencia óptima en cualquier dispositivo.

---

## 1️⃣ ESTRUCTURA TÉCNICA FUNDAMENTAL

### Viewport & Responsividad
```html
<meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" 
      name="viewport" />
```
- **width=device-width**: Se adapta al ancho del dispositivo
- **initial-scale=1.0**: Sin zoom inicial
- **user-scalable=no**: Previene zoom manual (la app controla la escala)

### Tecnostack Frontend
- **Tailwind CSS** (`https://cdn.tailwindcss.com`): Framework de utilidad para estilos responsive
- **Google Fonts - Inter**: Tipografía profesional (pesos: 400, 500, 600, 700, 900)
- **Material Symbols Outlined**: Iconografía moderna de Google
- **Vanilla JavaScript**: Interactividad sin dependencias externas

---

## 2️⃣ SISTEMA DE DISEÑO (DESIGN SYSTEM)

### 🎨 Paleta de Colores Oficial

#### Brand Identity
- **Brand Lilac**: `#5A4B9E` → Solo para logo e identidad

#### UI Principal (OBLIGATORIO)
- **UI Primary**: `#5B55C8` → Color de acciones principales
- **UI Primary Hover**: `#4A45B0` → Estados hover/active
- **Soft Highlight**: `#EFEEFF` → Tints y highlights

#### Escala de Grises (Neutrales)
```
jom-gray-900: #1F2937  ← Texto principal (neutral-text)
jom-gray-800: #374151
jom-gray-700: #4B5563
jom-gray-600: #6B7280  ← Texto secundario (neutral-secondary)
jom-gray-500: #6B7280
jom-gray-400: #9CA3AF
jom-gray-300: #D1D5DB
jom-gray-200: #E5E7EB  ← Bordes (neutral-border)
jom-gray-100: #F3F4F6
jom-gray-50:  #F8F9FC  ← Fondos claros (neutral-bg)
```

#### Colores Semánticos
- **Success**: `#16A34A` → Confirmaciones, estados positivos
- **JOM Gold**: `#FDB022` → Acentos premium
- **Background Light**: `#f6f6f8`
- **Background Dark**: `#14141e`

### 📐 Espaciado & Border Radius (Tailwind Config)
```javascript
borderRadius: {
  "jom": "12px",           // Inputs, botones pequeños
  "card": "16px",          // Tarjetas, modales
  "jom-input": "12px"      // Campos de formulario
}
```

### 🔤 Tipografía
- **Font Family**: Inter (sans-serif)
- **Font Weights**: 400 (regular), 500 (medium), 600 (semibold), 700 (bold), 900 (black)
- **Antialiasing**: `-webkit-font-smoothing: antialiased`

### 🎭 Sombras (Shadow System)
```css
.search-shadow {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), 0 4px 16px rgba(0, 0, 0, 0.04);
}
.card-shadow {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}
.destacada {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}
```

---

## 3️⃣ BREAKPOINTS & ESTRATEGIA RESPONSIVE

### Tailwind Breakpoints Utilizados
```
xs: 0px      ← Por defecto (móvil)
sm: 640px    ← Tablets pequeñas
md: 768px    ← Tablets estándar / Desktop menor
lg: 1024px   ← Desktop
xl: 1280px   ← Desktop grande
2xl: 1536px  ← Pantallas muy grandes
```

### Max Content Width
```css
.max-content-width {
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  
  /* Mobile: 16px padding */
  padding-left: 16px;
  padding-right: 16px;
  
  /* Tablet+ : 32px padding */
  @media (min-width: 768px) {
    padding-left: 32px;
    padding-right: 32px;
  }
}
```

### Patrón Mobile-First
- Estilos base para móvil (xs)
- Modificadores con `md:`, `lg:`, `xl:` para pantallas mayores
- Ejemplo: `p-3 md:p-4` = 12px móvil, 16px tablet+

---

## 4️⃣ COMPONENTES CORE

### Header Sticky Responsive
```html
<header class="sticky top-0 z-50 bg-white border-b border-neutral-border">
  <div class="px-4 h-14 flex items-center justify-between">
    <!-- Logo -->
    <div class="text-primary font-bold text-xl tracking-tight">jom</div>
    
    <!-- Botones: Cuenta + Menú (solo mobile) -->
    <div class="flex items-center gap-2">
      <button class="w-9 h-9 flex items-center justify-center rounded-full ...">
        <span class="material-symbols-outlined">account_circle</span>
      </button>
      <button class="w-9 h-9 flex items-center justify-center md:hidden ...">
        <span class="material-symbols-outlined">menu</span>
      </button>
    </div>
  </div>
</header>
```

**Comportamiento Responsive**:
- Altura: `h-14` (56px móvil) → `md:h-20` (80px desktop)
- Botón menú hamburguesa: visible en móvil → `md:hidden` en desktop
- Padding: `px-4` (móvil) → `md:px-8` (desktop)
- Z-index: 50 (por debajo de modales)

### Cards / Tarjetas
```html
<div class="bg-white rounded-[16px] border border-[#E5E7EB] 
            p-3 md:p-4 
            flex flex-col md:flex-row 
            shadow-destacada">
  
  <!-- Imagen: Full width móvil, 180px desktop -->
  <div class="w-full md:w-[180px] aspect-[16/10] md:aspect-auto md:h-[120px] 
              rounded-[12px] overflow-hidden flex-shrink-0">
    <img alt="" class="w-full h-full object-cover" src="..." />
  </div>
  
  <!-- Contenido: Apilado móvil, lado a lado desktop -->
  <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-6">
    <!-- Texto content -->
  </div>
</div>
```

**Comportamiento**:
- Móvil: Flex column (vertical), imagen full width
- Desktop: Flex row (horizontal), imagen fija 180px
- Padding adaptable: `p-3` → `md:p-4`

### Botones & CTA
```html
<!-- Botón Primario -->
<button class="px-6 py-3 rounded-[12px] 
               bg-primary hover:bg-primary-hover active:scale-95 
               text-white font-semibold 
               text-[14px] md:text-[16px]
               transition-all duration-200">
  Reservar Ahora
</button>

<!-- Botón Terciario (texto) -->
<button class="text-primary hover:text-primary-hover 
               text-[14px] md:text-[16px] font-semibold
               active:scale-95 transition-colors">
  Ver Detalle
  <span class="material-symbols-outlined text-[18px]">chevron_right</span>
</button>
```

**Estados de Interacción**:
- `hover:bg-color` → Cambio color hover
- `active:scale-95` → Efecto press (95% escala)
- `transition-all duration-200` → Suavidad 200ms

### Inputs & Formularios
```html
<input type="text" 
       class="w-full bg-neutral-bg rounded-[12px] 
              px-4 py-3 
              border border-neutral-border
              text-[14px] md:text-[16px]
              placeholder-neutral-secondary
              focus:border-primary focus:outline-primary
              transition-colors" 
       placeholder="Tu email" />
```

---

## 5️⃣ PÁGINAS MOBILE (ANÁLISIS DETALLADO)

### 📄 1. M-HOME-PAGE.html (Página de Inicio)

#### Secciones
**A) Header Sticky (56px móvil)**
```
[Logo JOM] → [Cuenta] [Menú]
```
- Logo: 24px bold, color primario
- Cuenta: Ícono circular 36px
- Menú: Hamburguesa, `md:hidden`

**B) Hero Section (Full-width gradient)**
```html
<header class="bg-gradient-to-b from-[#F8F9FC] to-[#EFEEFF] pt-8 pb-8">
  <h1 class="text-2xl font-semibold">
    Reserva tu <span class="text-primary">Hospedaje</span>
  </h1>
  <p class="text-neutral-secondary text-sm">Descubre lugares increíbles</p>
</header>
```
- Título: 22px móvil → 28px desktop
- Subtítulo: 14px, gris neutral
- Fondo: Gradiente suave purpura

**C) Buscador / Search Bar**
```html
<button class="w-full bg-neutral-gray rounded-full p-3 
               flex items-center gap-3">
  <span class="material-symbols-outlined">search</span>
  <div>
    <p class="text-sm font-semibold">Santa Cruz de la Sierra</p>
    <p class="text-xs text-text-muted">03 feb - 13 feb · 1 huésped</p>
  </div>
</button>
```
- Input full-width con bordes redondeados
- Ícono búsqueda + texto de destino
- Fecha + cantidad huéspedes (dos líneas)
- Fondo: `neutral-gray` (#F8F9FC)

**D) Categorías (Horizontal Scroll)**
```html
<div class="flex gap-3 overflow-x-auto hide-scrollbar pb-1">
  <button class="flex-shrink-0 px-4 py-2 rounded-full 
                 bg-neutral-bg text-neutral-text 
                 hover:bg-neutral-text hover:text-white
                 transition-colors">
    🏠 Casas
  </button>
  <!-- Más categorías -->
</div>
```
- Scroll horizontal sin scrollbar
- Pills/Tags con hover state
- Emojis + etiqueta de categoría

**E) Grid de Propiedades Destacadas**
```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6">
  <div class="rounded-card overflow-hidden">
    <img class="w-full h-48 md:h-56 object-cover" src="..." />
    <div class="p-4">
      <h3 class="font-semibold text-neutral-text">Penthouse...</h3>
      <p class="text-sm text-neutral-secondary">⭐ 4.8 (120 reseñas)</p>
      <p class="text-lg font-bold text-primary">$280/noche</p>
    </div>
  </div>
</div>
```
- Móvil: 1 columna (full-width)
- Tablet+: 3 columnas con gap 24px
- Imagen: 192px altura móvil
- Rating: ⭐ + número reseñas

**F) Bottom Sheet Modal**
```javascript
// Controla login, registro y menú lateral
.login-sheet {        // Modal login
  transform: translateY(100%);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.login-sheet.active { transform: translateY(0); }

.register-sheet {     // Modal registro
  transform: translateY(100%);
}
.register-sheet.active { transform: translateY(0); }
```

---

### 📄 2. M-BUSQUEDA.HTML (Búsqueda & Resultados)

#### Layout de Layers (Z-Index)

**Header Sticky** (`z-50`)
```
[← Atrás] [Logo jom] [🔧 Filtros]
```
- Botón atrás: `onclick="window.history.back()"`
- Filtros: Ícono tune (ajustes)

**Search Bar Sticky** (`z-40`, debajo del header)
```html
<div class="sticky top-14 z-40 bg-white px-4 py-3 search-shadow">
  <button class="w-full bg-neutral-gray rounded-full p-3 
                 flex items-center gap-3" onclick="openSearchModal()">
    <span class="material-symbols-outlined text-text-muted">search</span>
    <div class="flex-1">
      <p class="text-sm font-semibold">Santa Cruz de la Sierra</p>
      <p class="text-xs text-text-muted">03 feb - 13 feb · 1 huésped</p>
    </div>
  </button>
</div>
```

**Resultados (Flujo)**
```
1. "X resultados encontrados" (contador)
2. Botones filtros horizontales (pills):
   - "Populares" (default)
   - "Más baratos"
   - "Mejor rated"
   - "+ filtros"
3. Grid de propiedades
```

#### Grid de Propiedades (Responsive)
```html
<div class="grid grid-cols-1 md:grid-cols-4 gap-4 md:gap-6">
  <!-- Cada propiedad: Card full-responsive -->
  <div class="rounded-large bg-white 
              hover:shadow-lg transition-shadow">
    <div class="relative h-48 md:h-56 overflow-hidden">
      <!-- Carrusel de imágenes con swipe indicators -->
      <div class="swipe-indicator">
        <div class="swipe-dot active"></div>
        <div class="swipe-dot"></div>
        <div class="swipe-dot"></div>
      </div>
    </div>
  </div>
</div>
```

**Carrusel de Imágenes (Mobile)**
```css
.swipe-indicator {
  position: absolute;
  bottom: 12px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 6px;
  z-index: 10;
}

.swipe-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.5);
  transition: all 0.3s;
}

.swipe-dot.active {
  background-color: white;
  width: 20px;
  border-radius: 3px;
}
```
- 3 puntos: 6px de diámetro
- Punto activo: Se expande a 20px × 6px
- Fondo blanco semi-transparente

---

### 📄 3. M-DETALLE-ANUNCIO.HTML (Detalles de Propiedad)

#### Layout Móvil vs Desktop

**MÓVIL (<768px)**
```
1. Imagen full-screen (30vh)
   ├─ [← Atrás] (esquina superior izquierda)
   └─ [Compartir] [♡ Favorito] (esquina superior derecha)

2. Título + ubicación (bajo imagen)
   "Tarija Hermosa Casa - Tarija, Bolivia"

3. Información detallada
   ├─ Precio: $280/noche
   ├─ Rating: ⭐ 4.8 (120 reseñas)
   ├─ Descripción
   ├─ Amenidades (grid)
   └─ Host info

4. STICKY FOOTER BAR (56px)
   [Precio] [Reservar]
```

**DESKTOP (≥768px)**
```
1. Grid de imágenes 2x2
   ├─ Foto principal: 2×2 (dominante)
   ├─ Secundarias: 1×1 (4 fotos)

2. Contenido al lado
   ├─ Título
   ├─ Precio + Rating
   ├─ Descripción extendida
   ├─ Amenidades
   └─ Host info (card separada)

3. Sin footer sticky (contenido integrado)
```

#### Galería Responsive
```html
<!-- MOBILE: 1 imagen -->
<div class="md:hidden relative w-full h-[30vh]">
  <img alt="Main Photo" class="w-full h-full object-cover" src="..." />
  <div class="absolute top-4 left-4">
    <button onclick="history.back()" 
            class="w-9 h-9 rounded-full bg-white/90 
                   backdrop-blur-sm flex items-center justify-center">
      <span class="material-symbols-outlined">arrow_back</span>
    </button>
  </div>
  <div class="absolute top-4 right-4 flex gap-2">
    <button class="w-9 h-9 rounded-full bg-white/90 ...">
      <span class="material-symbols-outlined">share</span>
    </button>
    <button class="w-9 h-9 rounded-full bg-white/90 ...">
      <span class="material-symbols-outlined">favorite_border</span>
    </button>
  </div>
</div>

<!-- DESKTOP: Grid 2×2 -->
<div class="hidden md:grid grid-cols-4 grid-rows-2 gap-3 
            md:h-[400px] rounded-2xl overflow-hidden">
  <div class="col-span-2 row-span-2">
    <img class="w-full h-full object-cover" src="..." />
  </div>
  <div class="col-span-1 row-span-1">
    <img class="w-full h-full object-cover" src="..." />
  </div>
  <!-- Más imágenes -->
</div>
```

#### Botones Flotantes Móvil
```html
<div class="absolute top-4 right-4 flex items-center gap-2">
  <button class="w-9 h-9 rounded-full 
                 bg-white/90 backdrop-blur-sm 
                 flex items-center justify-center 
                 shadow-lg active:scale-90 
                 transition-transform">
    <span class="material-symbols-outlined">share</span>
  </button>
  <button class="w-9 h-9 rounded-full ...">
    <span class="material-symbols-outlined">favorite_border</span>
  </button>
</div>
```
- Fondo: `bg-white/90` (90% opacidad)
- Desenfoque: `backdrop-blur-sm`
- Sombra: `shadow-lg`
- Efecto press: `active:scale-90`

---

### 📄 4. M-PAGINA-VIAJES.HTML (Mis Viajes / Reservas)

#### Estructura
```html
<!-- Header -->
<header class="sticky top-0 z-50 h-14 md:h-20">
  [Logo] [Botones]
</header>

<!-- Título -->
<h1 class="text-[22px] md:text-[28px] font-semibold">Viajes</h1>

<!-- Tabs Navigation -->
<div class="flex gap-6 md:gap-8 border-b border-neutral-border mb-4">
  <button class="pb-3 md:pb-4 text-[14px] md:text-[16px] font-semibold
                 text-primary border-b-2 border-primary">
    Mis reservas
  </button>
  <button class="pb-3 md:pb-4 text-[14px] md:text-[16px] font-medium
                 text-neutral-secondary hover:text-neutral-text">
    Reseñas pendientes
  </button>
</div>

<!-- Lista de Reservas -->
<div class="flex flex-col gap-4 md:gap-6">
  <!-- Cards de reservas -->
</div>
```

#### Card de Reserva Responsive
```html
<div class="bg-white rounded-[16px] border border-[#E5E7EB] 
            p-3 md:p-4 
            flex flex-col md:flex-row md:items-center md:justify-between
            shadow-destacada">
  
  <!-- Contenedor principal: Vertical móvil, horizontal desktop -->
  <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-6">
    
    <!-- Imagen: Full-width móvil, 180px desktop -->
    <div class="w-full md:w-[180px] aspect-[16/10] md:aspect-auto md:h-[120px] 
                rounded-[12px] overflow-hidden flex-shrink-0">
      <img alt="Property" class="w-full h-full object-cover" src="..." />
    </div>
    
    <!-- Información -->
    <div class="flex flex-col gap-2">
      <div class="flex items-center gap-2 md:gap-3 flex-wrap">
        <h3 class="text-[15px] md:text-[16px] font-semibold 
                   text-neutral-text">Penthouse con vista al mar</h3>
        <span class="px-2.5 md:px-3 py-1 rounded-full 
                     text-[11px] md:text-[12px] font-bold 
                     bg-green-100 text-success">En curso</span>
      </div>
      <div class="flex items-center gap-2 text-neutral-secondary">
        <span class="material-symbols-outlined text-[18px]">calendar_today</span>
        <p class="text-[13px] md:text-[14px]">12 - 18 Octubre, 2024</p>
      </div>
    </div>
  </div>
  
  <!-- CTA Link -->
  <a class="flex items-center justify-center md:justify-start gap-1 
           text-[14px] font-semibold text-[#5B55C8] 
           hover:opacity-80 transition-opacity 
           mt-3 md:mt-0 md:pr-4 active:scale-95" href="#">
    Ver detalle
    <span class="material-symbols-outlined text-[18px]">chevron_right</span>
  </a>
</div>
```

**Badge de Estado**
```
Estados posibles:
- "En curso" → Verde (#16A34A background, bg-green-100)
- "Completado" → Gris
- "Cancelado" → Rojo
```

---

### 📄 5. M-CONFIGURACION.HTML (Ajustes de Cuenta)

#### Layout Secciones
```html
<div class="px-4 py-6 md:py-8">
  <h1 class="text-[22px] md:text-[28px] font-semibold mb-6">Configuración</h1>
  
  <!-- Secciones apiladas -->
  <div class="flex flex-col gap-6 md:gap-8">
    
    <!-- Sección 1: Perfil -->
    <section class="card-section border border-neutral-border rounded-card">
      <div class="p-4 md:p-6">
        <div class="flex items-center gap-4">
          <img class="w-16 h-16 rounded-full object-cover" src="..." />
          <div>
            <h3 class="font-semibold text-neutral-text">Juan Pérez</h3>
            <p class="text-sm text-neutral-secondary">juan@example.com</p>
          </div>
        </div>
      </div>
    </section>
    
    <!-- Sección 2: Opciones menú -->
    <section>
      <div class="dropdown-item">
        <span class="material-symbols-outlined">person</span>
        <span>Editar perfil</span>
      </div>
      <div class="dropdown-item">
        <span class="material-symbols-outlined">lock</span>
        <span>Cambiar contraseña</span>
      </div>
      <!-- Más items -->
    </section>
  </div>
</div>
```

#### Dropdown Item Hover
```css
.dropdown-item {
  height: 48px;
  display: flex;
  align-items: center;
  padding: 0 20px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  color: #1F2937;
  gap: 12px;
  border-left: 3px solid transparent;
  transition: all 0.2s ease;
}

.dropdown-item:hover {
  background-color: #EFEEFF;      /* Soft highlight */
  border-left-color: #5B55C8;     /* Primary color */
  color: #5B55C8;                 /* Primary text */
}
```

---

### 📄 6. M-MODAL-LOGIN.HTML (Modal Autenticación)

#### Estructura Overlay
```html
<!-- Overlay backdrop -->
<div class="fixed inset-0 z-0 flex items-center justify-center p-8 pointer-events-none">
  <div class="absolute top-1/4 left-1/4 w-48 h-48 bg-primary/20 rounded-full blur-3xl"></div>
  <div class="absolute bottom-1/4 right-1/4 w-64 h-64 bg-primary/10 rounded-full blur-3xl"></div>
</div>

<!-- Dimmer capa -->
<div class="fixed inset-0 z-10 backdrop-blur-xl bg-black/10 dark:bg-black/40"></div>

<!-- Modal container -->
<div class="fixed inset-0 z-20 flex items-end sm:items-center justify-center">
  <div class="relative w-full sm:max-w-[440px] 
              bg-white sm:rounded-lg rounded-t-[24px] 
              shadow-2xl overflow-hidden animate-slide-up">
    <!-- Botón cerrar -->
    <button class="absolute right-2 top-2 z-10">
      <span class="material-symbols-outlined">close</span>
    </button>
    
    <!-- Contenido -->
    <div class="px-6 sm:px-8 py-8 sm:py-6">
      <!-- Form -->
    </div>
  </div>
</div>
```

**Animación de Entrada**
```css
@keyframes slideUp {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(0);
  }
}

.animate-slide-up {
  animation: slideUp 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

**Comportamiento Responsive**:
- **Móvil**: Modal desde el fondo (bottom-sheet)
  - Ancho: 100%
  - Border radius: `rounded-t-[24px]` (solo arriba)
  
- **Desktop (sm)**: Modal centrado
  - Ancho: máximo 440px
  - Border radius: `rounded-lg` (todos los lados)

---

### 📄 7. M-CONTACTAR-ANFITRION.HTML (Mensajería)

```html
<div class="flex flex-col h-screen">
  <!-- Header: Sticky -->
  <header class="sticky top-0 z-40 bg-white border-b 
                 px-4 h-14 flex items-center">
    <button class="w-9 h-9 flex items-center justify-center">
      <span class="material-symbols-outlined">arrow_back</span>
    </button>
    <div class="flex-1 px-4">
      <h3 class="font-semibold text-neutral-text">Carlos Mendoza</h3>
      <p class="text-xs text-neutral-secondary">Anfitrión de Tarija Hermosa Casa</p>
    </div>
    <button class="w-9 h-9 flex items-center justify-center">
      <span class="material-symbols-outlined">more_vert</span>
    </button>
  </header>
  
  <!-- Área de mensajes: Scrollable -->
  <div class="flex-1 overflow-y-auto px-4 py-4 space-y-4">
    <!-- Mensajes de anfitrión (izquierda) -->
    <div class="flex gap-2">
      <img class="w-8 h-8 rounded-full" src="..." />
      <div class="bg-jom-gray-100 rounded-lg p-3 max-w-xs">
        <p class="text-sm text-neutral-text">¡Hola! Bienvenido a mi casa...</p>
      </div>
    </div>
    
    <!-- Mensajes del usuario (derecha) -->
    <div class="flex justify-end gap-2">
      <div class="bg-primary text-white rounded-lg p-3 max-w-xs">
        <p class="text-sm">¡Gracias! Llego mañana...</p>
      </div>
    </div>
  </div>
  
  <!-- Input sticky (abajo) -->
  <div class="sticky bottom-0 bg-white border-t px-4 py-3 flex gap-2">
    <input class="flex-1 bg-jom-gray-100 rounded-full px-4 py-3 
                   text-sm placeholder-neutral-secondary" 
           placeholder="Escribe un mensaje..." />
    <button class="w-10 h-10 rounded-full bg-primary flex items-center justify-center 
                   text-white active:scale-90 transition-transform">
      <span class="material-symbols-outlined">send</span>
    </button>
  </div>
</div>
```

---

## 6️⃣ PATRONES DE INTERACCIÓN

### 🎯 Touch & Feedback

#### Ripple / Press Effect
```css
active:scale-95      /* Botones se encogen al presionar */
transition-all duration-200
```

#### Hover States (Desktop)
```css
hover:bg-neutral-bg
hover:text-primary
hover:opacity-80
hover:shadow-lg
```

#### Focus States (Accesibilidad)
```css
focus:border-primary
focus:outline-primary
focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-primary
```

### 🚀 Animaciones CSS

#### Slide Up (Modales)
```css
@keyframes slideUp {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}
.animate-slide-up { animation: slideUp 0.3s ease-out; }
```

#### Menu Sidebar (Mobile)
```css
.menu-sidebar {
  transform: translateX(100%);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.menu-sidebar.active {
  transform: translateX(0);
}
```

#### Acordeón (Expand/Collapse)
```css
.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease, padding 0.3s ease;
}
.accordion-content.active {
  max-height: 500px;
  padding-top: 16px;
}

.accordion-button.active .material-symbols-outlined {
  transform: rotate(180deg);
}
```

### 🎭 Tooltip / Light Dismiss

```javascript
// Cerrar al hacer click fuera
element.addEventListener('click', (e) => {
  if (!dropdown.contains(e.target)) {
    dropdown.classList.remove('active');
  }
});
```

---

## 7️⃣ CARACTERÍSTICAS AVANZADAS

### 📸 Carrusel con Swipe Indicators
```html
<div class="relative h-48 md:h-56 overflow-hidden">
  <div id="carousel" class="flex transition-transform duration-300">
    <img class="w-full h-full object-cover flex-shrink-0" src="img1.jpg" />
    <img class="w-full h-full object-cover flex-shrink-0" src="img2.jpg" />
    <img class="w-full h-full object-cover flex-shrink-0" src="img3.jpg" />
  </div>
  
  <div class="swipe-indicator">
    <div class="swipe-dot active"></div>
    <div class="swipe-dot"></div>
    <div class="swipe-dot"></div>
  </div>
</div>
```

### 🔍 Search Modal con Focus

```html
<div class="modal" id="searchModal">
  <div class="px-4 py-4">
    <div class="flex items-center bg-neutral-gray rounded-full px-4">
      <input class="flex-1 bg-transparent py-3 text-neutral-text 
                     placeholder-neutral-secondary focus:outline-none" 
             placeholder="¿Dónde quieres ir?" autofocus />
      <button onclick="closeSearch()">
        <span class="material-symbols-outlined">close</span>
      </button>
    </div>
  </div>
</div>
```

### 📍 Maps Integration
```html
<div id="map" class="w-full h-80 rounded-lg overflow-hidden"></div>

<script async src="https://maps.googleapis.com/maps/api/js?key=..."></script>
<script>
  const map = new google.maps.Map(document.getElementById('map'), {
    zoom: 13,
    center: { lat: -19.6345, lng: -65.2519 }
  });
</script>
```

### 🌙 Dark Mode (Preparado)
```html
<html class="light" lang="es">
  <!-- Cambiar a "light" o "dark" -->
</html>

<style>
  .dark {
    background-color: #14141e;
  }
  .dark .bg-pattern {
    background-color: #14141e;
    background-image: radial-gradient(#2d2d3d 1px, transparent 1px);
  }
</style>
```

---

## 8️⃣ OPTIMIZACIONES MOBILE

### ⚡ Performance
- **Lazy Loading**: Imágenes fuera de viewport con `loading="lazy"`
- **Preconnect**: `<link rel="preconnect" href="https://fonts.gstatic.com">`
- **Críticos prioritarios**: Fonts, colores, estructura
- **No bloqueantes**: Scripts async

### 📱 Tactile UX
- **Touch targets mínimo**: 44×44px (recomendado)
- **No scroll-jank**: Transition suave con GPU (transform, opacity)
- **Tap feedback**: `active:scale-95`, color changes
- **Tap highlight**: `*{ -webkit-tap-highlight-color: transparent; }`

### 🔄 Viewport & Scroll
```html
<meta content="width=device-width, initial-scale=1.0, 
       maximum-scale=1.0, user-scalable=no" name="viewport" />
```
- Sin pinch zoom (mejor control)
- Zoom inicial 1.0 (tamaño natural)

### 🌐 Semántica HTML
```html
<button class="...">   <!-- Teclado accesible -->
<nav class="...">      <!-- Navegación semántica -->
<header class="...">   <!-- Encabezado -->
<main class="...">     <!-- Contenido principal (solo 1) -->
<footer class="...">   <!-- Pie de página -->
```

---

## 9️⃣ SISTEMA DE GRID RESPONSIVE

### Ejemplos de Grid Adaptables

**1. De 1 → 2 → 3 → 4 columnas**
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-4 gap-4 md:gap-6">
  <div>Card</div>
</div>
```

**2. Hero + Sidebar (Mobile stack)**
```html
<div class="flex flex-col lg:flex-row gap-8">
  <div class="flex-1">Hero content</div>    <!-- Full width móvil -->
  <div class="w-full lg:w-80">Sidebar</div> <!-- 320px desktop, full móvil -->
</div>
```

**3. Galería Masonry Mobile**
```html
<div class="columns-1 md:columns-2 lg:columns-3 gap-4">
  <img class="w-full mb-4 rounded-lg" src="..." />
  <!-- Se distribuye automáticamente -->
</div>
```

---

## 🔟 CONVENCIONES DE CÓDIGO

### Orden de Clases Tailwind (BEM-like)
```html
<!-- Estructura → Display → Spacing → Sizing → Typography → Colors → Effects -->
<div class="
  flex flex-col
  px-4 py-3 gap-2
  w-full
  text-sm font-semibold
  text-neutral-text
  rounded-lg hover:bg-primary
">
```

### Variables de Color Reutilizables
```javascript
const colors = {
  primary: "#5B55C8",
  primaryHover: "#4A45B0",
  neutralText: "#1F2937",
  neutralSecondary: "#6B7280",
  neutralBorder: "#E5E7EB",
  neutralBg: "#F8F9FC",
  success: "#16A34A"
};
```

### Estructura de Archivos
```
MOBILE/
├── M-HOME-PAGE.html           ← Landing
├── M-BUSQUEDA.HTML            ← Search + Results
├── M-DETALLE-ANUNCIO.HTML     ← Property details
├── M-PAGINA-VIAJES.HTML       ← My trips
├── M-CONFIGURACION.HTML       ← Settings
├── M-MODAL-LOGIN.HTML         ← Auth modal
├── M-CONTACTAR-ANFITRION.HTML ← Messaging
├── M-ANFITRION-DETALLE.HTML   ← Host profile
├── M-METODOS-PAGO.HTML        ← Payment methods
└── reglas.txt                 ← Design tokens
```

---

## 🎯 RESUMEN: PRINCIPIOS MOBILE-FIRST DE JOM

✅ **Viewport correcto**: Evita zoom involuntario
✅ **Media queries ordenadas**: Mobile-first (xs → md → lg)
✅ **Touch-friendly**: Targets ≥ 44px
✅ **Feedback visual**: Hover, active, transitions
✅ **Máximo 1200px ancho**: Legibilidad en desktop
✅ **Imágenes responsive**: `object-cover`, aspect ratio
✅ **Tipografía escalable**: 14px→16px móvil→desktop
✅ **Colores consistentes**: Sistema oficial de 4 colores
✅ **Animaciones suaves**: 0.3s cubic-bezier
✅ **Sin frameworks pesados**: Vanilla JS + Tailwind

---

## 📞 NOTAS TÉCNICAS FINALES

### Compatibilidad Browser
- Chrome/Edge ✅ (latest)
- Firefox ✅ (latest)
- Safari ✅ (iOS 14+)
- Samsung Internet ✅ (14+)

### Librerías Externas
- Tailwind CSS CDN (no build requerido)
- Google Fonts (Inter)
- Google Material Symbols
- Google Maps API (algunas páginas)

### Performance Metrics Target
- **First Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **Time to Interactive**: < 3.5s

---

**Documento generado: 18 de Febrero 2026** 📱💜
