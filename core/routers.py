from rest_framework import routers


class InternalAPIRouter(routers.DefaultRouter):
    """Extends `DefaultRouter` class to add a method for extending url routes
    from another router."""

    def extend(self, router: routers.SimpleRouter) -> None:
        self.registry.extend(router.registry)
