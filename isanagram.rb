def is_anagram()
puts "**************************************"
puts "Put line 1:"
puts "**************************************"
line1 = gets.chomp

puts "**************************************"
puts "Put line 2:"
puts "**************************************"
line2 = gets.chomp

line1sig = line1.upcase.gsub(/\W+/,'').split(//).sort.join()
line2sig = line2.upcase.gsub(/\W+/,'').split(//).sort.join()

#puts line1sig
#puts line2sig
#puts line1sig == line2sig
end

a = File.open("spsidebyside2.txt")

line_array_odd = []
line_array_even = []
line_no = 0
a.each do |thisline|
  if line_no % 2 == 0
    line_array_even.push(thisline)
  else
    line_array_odd.push(thisline)
  end
  line_no += 1
  #puts line_no
end
puts "*********************************************"
line_no = 0
line_array_even.each do |thisline|
  #puts line_no
  line1 = line_array_even[line_no]
  line2 =  line_array_odd[line_no]
line1sig = line1.upcase.gsub(/\W+/,'').split(//).sort.join()
line2sig = line2.upcase.gsub(/\W+/,'').split(//).sort.join()
  if line1sig != line2sig
    puts "OOPS"
    puts line1
    puts line1sig
    puts line2
    puts line2sig
    hash1 = {}
    hash2 = {}
    line1sig.split(//).each do |thisletter|
      if hash1[thisletter]
        hash1[thisletter] += 1
      else
        hash1[thisletter] = 1
      end
    end
    line2sig.split(//).each do |thisletter|
      if hash2[thisletter]
        hash2[thisletter] += 1
      else
        hash2[thisletter] = 1
      end
    end
    puts(hash1)
    puts(hash2)
  end
  line_no += 1
end

