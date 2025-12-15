# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('..'))

# -- Основная информация о проекте -------------------------------------------------
project = 'lab-git-demo'  # Название вашего проекта
author = 'Kvanden1'       # Ваше имя
copyright = f'{datetime.now().year}, {author}'  # Авторские права с текущим годом
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Настройки версий -------------------------------------------------------------
# Это разделение на version/release используется для подстановки |version| и |release| в тексте
version = '1.0'  # Короткая версия (например, основная)
release = '1.0.0'  # Полная версия (например, с номером сборки)

# -- Настройки времени сборки -----------------------------------------------------
# Формат для отображения даты/времени последнего обновления в сгенерированном HTML
html_last_updated_fmt = '%d.%m.%Y, %H:%M'

# -- Расширения Sphinx ------------------------------------------------------------
# Добавляем расширения для дополнительных функций
extensions = [
    'sphinx.ext.autodoc',    # Автоматическое документирование из docstrings
    'sphinx.ext.githubpages', # Помогает публикации на GitHub Pages
]

# -- Настройки вывода HTML --------------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Тема "Read the Docs"
