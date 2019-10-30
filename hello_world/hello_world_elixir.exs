"Hello World"
|> String.graphemes
|> Enum.map(fn char -> char <> "\n" end)
|> Enum.reduce(
  { "", "" },
  fn next_char, { spaces, text } -> 
    { spaces <> " ", text <> spaces <> next_char }
  end
)
|> elem(1)
|> IO.puts
