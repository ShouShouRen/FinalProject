interface Window {
  pywebview: {
    api: {
      get_children(path: React.Key): Promise<string>;
    };
  };
}
