# config_manager_impl.py
from __future__ import annotations
import threading
from typing import Type, Any, Optional

from .config_manager import FileBasedConfigurationManager


class FileBasedConfigurationManagerImpl(FileBasedConfigurationManager):
    """
    Thread-safe lazy singleton concrete implementation of FileBasedConfigurationManager.
    Use FileBasedConfigurationManagerImpl.get_instance() to obtain the singleton.
    """

    # class-level singleton state
    _instance: Optional["FileBasedConfigurationManagerImpl"] = None
    _instance_lock = threading.Lock()

    def __init__(self) -> None:
        # Initialize base (it sets self.properties = {})
        super().__init__()
        # instance-level lock to protect self.properties concurrent access
        self._lock = threading.RLock()

    @staticmethod
    def get_instance() -> FileBasedConfigurationManager:
        """
        Return the singleton instance. Lazily creates it in a thread-safe manner.
        """
        # Fast path (no lock) for performance
        if FileBasedConfigurationManagerImpl._instance is None:
            with FileBasedConfigurationManagerImpl._instance_lock:
                if FileBasedConfigurationManagerImpl._instance is None:
                    FileBasedConfigurationManagerImpl._instance = FileBasedConfigurationManagerImpl()
        return FileBasedConfigurationManagerImpl._instance  # type: ignore[return-value]

    @staticmethod
    def reset_instance() -> None:
        """
        Reset the singleton instance. Useful for unit tests.
        """
        with FileBasedConfigurationManagerImpl._instance_lock:
            inst = FileBasedConfigurationManagerImpl._instance
            if inst is not None:
                # Try clearing to free memory/state
                try:
                    inst.clear()
                except Exception:
                    pass
            FileBasedConfigurationManagerImpl._instance = None

    # --- configuration API implementations ---

    def get_configuration(self, key: str) -> Optional[str]:
        """
        Return configuration value as string or None if not present.
        """
        with self._lock:
            return self.properties.get(key)

    def get_configuration_with_type(self, key: str, type_: Type) -> Any:
        """
        Retrieve configuration value and convert to requested type using base convert().
        Returns None if key not present. Raises ValueError if conversion fails.
        """
        val = self.get_configuration(key)
        if val is None:
            return None
        # convert (base class convert raises ValueError if conversion fails)
        return FileBasedConfigurationManager.convert(val, type_)

    def set_configuration(self, key: str, value: str) -> None:
        """
        Store the configuration value. Coerce non-string values to str to keep file-based semantics.
        """
        with self._lock:
            # store as string because base.properties: Dict[str,str]
            # Keep simple: coerce incoming value to str
            self.properties[key] = str(value)

    def remove_configuration(self, key: str) -> None:
        with self._lock:
            self.properties.pop(key, None)

    def clear(self) -> None:
        with self._lock:
            self.properties.clear()
