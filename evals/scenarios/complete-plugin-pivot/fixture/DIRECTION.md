# Current owner direction

Decision state: owner-ratified for this exercise.

The bookmark-cleaning CLI was an unshipped prototype. The product is now an
embedded URL normalization library called by multiple desktop and server hosts.

The target must:

- expose a deterministic function that accepts a URL string and returns either
  a normalized URL or a typed error;
- have no command-line, process-exit, environment-variable, config-file,
  printing, or process-global contract;
- preserve removal of a trailing slash and lowercasing of the host; and
- allow hosts to choose their own I/O, configuration, and error presentation.

There are no external CLI users, releases, or persistent data to migrate. The
owner will accept the first slice when two hosts can call the pure API and its
tests prove the required normalization without importing CLI or file-system
modules.
