interface Window {
  pywebview: {
    api: {
      get_local_children(path: React.Key): Promise<string>;
      get_server_children(path: React.Key): Promise<string>;
      login(host: string, port: string, username: string, password: string): Promise<string>;
    };
  };
}
