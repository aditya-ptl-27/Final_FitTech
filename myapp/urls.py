from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('chat/',views.chat,name='chat'),
    path('home_workouts/',views.home_workouts,name='home_workouts'),
    path('beginner_workouts/',views.beginner_workouts,name='beginner_workouts'),
    path('intermediate_workouts/',views.intermediate_workouts,name='intermediate_workouts'),
    path('advanced_workouts/',views.advanced_workouts,name='advanced_workouts'),
    path('full_body/',views.full_body,name='full_body'),
    path('lower_body/',views.lower_body,name='lower_body'),
    path('upper_body/',views.upper_body,name='upper_body'),
    path('get_fit/',views.get_fit,name='get_fit'),
    path('gain_strength/',views.gain_strength,name='gain_strength'),
    path('weight_loss/',views.weight_loss,name='weight_loss'),
    path('build_muscle/',views.build_muscle,name='build_muscle'),
    path('trainer_home_workouts/',views.trainer_home_workouts,name='trainer_home_workouts'),
    path('trainer/',views.trainer,name='trainer'),
    path('trainer_view_workouts/',views.trainer_view_workouts,name='trainer_view_workouts'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('profile/',views.profile,name='profile'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('update_password/',views.update_password,name='update_password'),
    path('trainer_index/',views.trainer_index,name='trainer_index'),
    path('trainer_add_workout/',views.trainer_add_workout,name='trainer_add_workout'),
    path('trainer_workout_detail/<int:pk>/',views.trainer_workout_detail,name='trainer_workout_detail'),
    path('trainer_workout_edit/<int:pk>/',views.trainer_workout_edit,name='trainer_workout_edit'),
    path('trainer_workout_delete/<int:pk>/',views.trainer_workout_delete,name='trainer_workout_delete'),
    path('trainer_profile/',views.trainer_profile,name='trainer_profile'),
    path('trainer_change_password/',views.trainer_change_password,name='trainer_change_password'),
    path('calculate_bmi/',views.calculate_bmi, name='calculate_bmi'),
    path('workout_detail/<int:pk>/',views.workout_detail, name='workout_detail'),
    path('ideal_body_weight/',views.ideal_body_weight, name='ideal_body_weight'),
    path('daily_calorie_intake/',views.daily_calorie_intake, name='daily_calorie_intake'),
    path('calories_burnt/',views.calories_burnt, name='calories_burnt'),
    path('trainer_view_blogs/',views.trainer_view_blogs,name='trainer_view_blogs'),
    path('trainer_add_blog/',views.trainer_add_blog,name='trainer_add_blog'),
    path('blog/',views.blog,name='blog'),
    path('trainer_blog_detail/<slug>',views.trainer_blog_detail, name="trainer_blog_detail"),
    path('blog_detail/<slug>',views.blog_detail, name="blog_detail"),
    path('trainer_blog_detail/<slug>',views.trainer_blog_detail, name="trainer_blog_detail"),
    path('trainer_blog_delete/<id>',views.trainer_blog_delete, name="trainer_blog_delete"),
    path('trainer_blog_edit/<slug>/',views.trainer_blog_edit, name="trainer_blog_edit"),
]
