# Current owner direction

Decision state: owner-ratified for this exercise.

The Python bookmark-cleaning CLI was an unshipped prototype. The product is now
a host-neutral WebAssembly component called by non-Python desktop and server
hosts. Those hosts load components through a versioned interface and cannot
embed a Python interpreter or expose process and file-system services.

The target must:

- expose a versioned component function that accepts a URL string and returns
  either a normalized URL or a typed error;
- have no command-line, process-exit, environment-variable, config-file,
  printing, Python-runtime, or process-global contract;
- preserve removal of a trailing slash and lowercasing of the host; and
- allow hosts to choose their own I/O, configuration, and error presentation.

There are no external CLI users, releases, or persistent data to migrate. The
owner will accept the first slice when two non-Python hosts can load the
component and call the pure API, and its tests prove the required normalization
without importing CLI, Python-runtime, or file-system dependencies.
