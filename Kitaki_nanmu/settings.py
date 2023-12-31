"""
Django settings for Kitaki_nanmu project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
"""
    密钥的配置，自动生成,随机值，一般用于数据的是加密处理，提高项目安全性
    主要用于：用户密码、CSRF机制（表单提交）、Session的数据加密
    一般不做修改
"""
SECRET_KEY = 'django-insecure-9#o7hg9ubar-32z51y4w5fmxuiwymv2xmt1h4)zeikt#wr)n5_'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
"""
    当为false时，ALLOWED_HOSTS必填，否则程序无法启动
"""
DEBUG = True
# 当项目存在上线时，DEBUG为FALSE，ALLOWED_HOSTS=['*']，如果想限制域名访问，就添加固定域名
# 为空时，项目只允许localhost和127。0.0.1访问
ALLOWED_HOSTS = []


# Application definition
"""
    主要是用于Django有哪些APP
"""
INSTALLED_APPS = [
    'django.contrib.admin', # 内置的用户后台管理系统
    'django.contrib.auth', # 用户认证系统
    'django.contrib.contenttypes', # 记录项目中所有的model元数据
    'django.contrib.sessions', # 会话功能，用于标识当前访问网站的用户身份，记录相关用户信息
    'django.contrib.messages', # 消息提示功能
    'django.contrib.staticfiles', # 查看静态文件路径
    # 添加x项目应用
    'index'
]
# 中间件配置，注意排列顺序。位置错误可能造成启动或运行失败
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 添加中间件，国际化和本地化功能
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Kitaki_nanmu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 设置模板文件夹路径，   多个项目应用可分开（列表形式），配置错误否则在项目运行时会无法生成相应的应用
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'index/templates'],
        # 添加index应用的模板文件, 一般都是如上写法
        # 'DIRS': [BASE_DIR / 'index/templates'],
        'APP_DIRS': True, # 是否再APP模板中查找文件
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Kitaki_nanmu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# 此处使用mysqlclient库方式连接，还可以使用pymysql的库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {'read_default_file':str(BASE_DIR / 'mysql.cnf')},
        # 'NAME': 'kitakinanmu',
        # 'USER': 'root',
        # 'PASSWORD': 'Cc@101204',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# 资源文件路由路径（CSS、JavaScript、图片等资源）    资源文件分为两种类型，静态资源和媒体资源
STATIC_URL = 'static/'  # 静态资源.   ,文件名可以更改，一般默认
# 镜头资源-媒体资源  当DEBUG为true时，会自动提供静态文件代理服务。 为false时不在提供服务
# STATIC_ROOT = 'BASE_DIR / static/' # 项目上线提供静态资源服务
# 资源集合 多个静态文件夹可以配置列表形式定义多个文件夹
# STATICFILES_DIRS = [BASE_DIR / 'static', BASE_DIR / 'index/XXX']

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
