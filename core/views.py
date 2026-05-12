from django.shortcuts import render

MI_PERFIL = {
    'mi_nombre': 'Carlos Alberto Vaca Lucio',
    'profesion': 'Ingeniero en Sotfware ',
    'email': 'cvaca9056@utm.edu.ec',
    'github': 'https://github.com/Dictadoor',
    'youtube': 'https://www.youtube.com/@dictadoor1806',
    'instagram': 'https://instagram.com/alberto_1806x',
    'tiktok': 'https://www.tiktok.com/@albertzzxz',
}

def portada(request):
    return render(request, 'core/index.html', MI_PERFIL)

def about(request):
    context = {
        **MI_PERFIL,
        'biografia': 'Nací el 18 de junio de 2003 en Esmeraldas. Actualmente estudio Ingeniería en Software en la Universidad Técnica de Manabí. Tengo un gran interés por la tecnología, razón por la cual elegí esta carrera. Me interesa entender cómo funcionan las cosas, desde la lógica hasta la implementación, y me esfuerzo cada día por mejorar mis habilidades en programación.',
        'biografia_extra': '',
    }
    return render(request, 'core/about.html', context)

def contact(request):
    context = {
        **MI_PERFIL,
        'descripcion_contacto': "Estoy abierto a oportunidades laborales, prácticas profesionales o colaboraciones en proyectos.",
        'telefono': '+593 98 341 5011',
        'honorarios': '20$/h',
    }
    return render(request, 'core/contact.html', context)