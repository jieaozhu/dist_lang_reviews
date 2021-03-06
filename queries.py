from incoq.runtime import *
CONFIG(
    obj_domain = 'true',
    default_impl = 'inc',
)
def strip(x):
    return x.strip()
def developers_with_more_than_one_project(ps):
    projects_python = Set()
    projects_github = Set()
    for p in ps:
        if 'python' in map(strip, p.language.lower().split(',')):
            projects_python.add(p)
        if 'github' in p.home_page:
            projects_github.add(p)
    print({p1.developer for p1 in projects_python if p1 in projects_github})
