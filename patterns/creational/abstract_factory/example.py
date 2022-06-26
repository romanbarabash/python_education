from abc import ABC, abstractmethod


class Browser(ABC):
    """
    Creates "Abstract Product A"
    """

    @abstractmethod
    def create_search_toolbar(self):
        pass

    @abstractmethod
    def create_browser_window(self):
        pass


class Messenger(ABC):
    """
    Creates "Abstract Product B"
    """

    @abstractmethod
    def create_messenger_window(self):
        pass


class VanillaBrowser(Browser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    def create_search_toolbar(self):
        print("Vanilla - Search Toolbar Created")

    def create_browser_window(self):
        print("Vanilla - Browser Window Created")


class VanillaMessenger(Messenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    def create_messenger_window(self):
        print("Vanilla - Messenger Window Created")


class SecureBrowser(Browser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    def create_search_toolbar(self):
        print("Secure - Search Toolbar Created")

    def create_browser_window(self):
        print("Secure - Browser Window Created")

    def create_incognito_mode(self):
        print("Secure - Incognito Mode Created")


class SecureMessenger(Messenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    def create_messenger_window(self):
        print("Secure - Messenger Window Created")

    def create_privacy_filter(self):
        print("Secure - Privacy Filter Created")

    def disappearing_messages(self):
        print("Secure - Disappearing Messages Feature Enabled")


class AbstractFactory(ABC):
    """
    The Abstract Factory
    """

    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass


class VanillaProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return VanillaBrowser()

    def create_messenger(self):
        return VanillaMessenger()


class SecureProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return SecureBrowser()

    def create_messenger(self):
        return SecureMessenger()


# app
for factory in (VanillaProductsFactory(), SecureProductsFactory()):
    browser_product = factory.create_browser()
    browser_messenger = factory.create_messenger()

    browser_product.create_browser_window()
    browser_product.create_search_toolbar()
    if isinstance(factory, SecureProductsFactory):
        browser_product.create_incognito_mode()  # only Secure browser can do

    browser_messenger.create_messenger_window()
    if isinstance(factory, SecureProductsFactory):
        browser_messenger.create_privacy_filter()  # only Secure browser can do

    print()

# abstract factory and abstract product ->
# create concrete factory ->
# create concrete product dependent of factory type (ex. Secure)
