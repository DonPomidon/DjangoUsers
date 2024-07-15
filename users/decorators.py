from django.contrib.auth.decorators import user_passes_test


def in_departments(user, departments):
    return user.is_superuser or user.groups.filter(name__in=departments).exists()


def department_required(*department_names):
    def in_department(user):
        return in_departments(user, department_names)
    return user_passes_test(in_department)
