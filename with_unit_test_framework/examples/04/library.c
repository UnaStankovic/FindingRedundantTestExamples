char* select_command(char* command_name) {
  if (!strcmp(command_name, "command1"))
    return "execute command1";
  else if (!strcmp(command_name, "command2"))
    return "execute command2";
  else if (!strcmp(command_name, "command3"))
    return "execute command3";
  return "unknown command";
}
