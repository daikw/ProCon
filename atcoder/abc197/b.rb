def count(str, index)
  res = tmp = 0; flg = false
  str.each_char.with_index do |c, i|
    # puts "#{c}, #{i}, #{flg}"    
    if c == '#' && flg
      res = tmp
      # puts res
      return res
    end
    flg = true if i == index
    tmp = 0 if c == '#'
    tmp += 1 if c == '.'
  end

  res = tmp
  # puts res
  res
end

if __FILE__ == $0
  h, w, x, y = gets.split.map(&:to_i)
  row = ''
  col = ''
  h.times do |i|
    tmp = gets
    col += tmp[y-1]
    row = tmp.strip if i == x-1
  end

  # puts "row: #{row}, #{row.length}"
  # puts "col: #{col}, #{col.length}"
  puts count(col, x-1) + count(row, y-1) - 1
end
