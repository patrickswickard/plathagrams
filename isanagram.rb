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


input_array = ARGV

if ARGV.length == 1
  a = File.open(ARGV[0])
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
elsif ARGV.length == 2
  a = File.open(ARGV[0])
  b = File.open(ARGV[1])
  line_array_odd = []
  line_array_even = []
  line_no = 0
  a.each do |thisline|
    line_array_odd.push(thisline)
    line_no += 1
    #puts line_no
  end
  b.each do |thisline|
    line_array_even.push(thisline)
    line_no += 1
    #puts line_no
  end
else
  raise 'Error'
end
puts "*********************************************"
line_no = 0
line_array_even.each do |thisline|
  #puts line_no
  line1 = line_array_even[line_no]
  line2 =  line_array_odd[line_no]
  line1sig = line1.to_s.upcase.gsub(/\W+/,'').split(//).sort.join()
  line2sig = line2.to_s.upcase.gsub(/\W+/,'').split(//).sort.join()
  line1siglength = line1sig.length
  line2siglength = line2sig.length
  #print "line1siglength #{line1siglength}\n"
  #print "line2siglength #{line2siglength}\n"
  if line1sig != line2sig
    puts line1
    puts line1sig
    puts line2
    puts line2sig
    hash1 = {}
    hash2 = {}
    lettercount1 = 0
    lettercount2 = 0
    line1sig.split(//).each do |thisletter|
      lettercount1 += 1
      if hash1[thisletter]
        hash1[thisletter] += 1
      else
        hash1[thisletter] = 1
      end
    end
    line2sig.split(//).each do |thisletter|
      lettercount2 += 1
      if hash2[thisletter]
        hash2[thisletter] += 1
      else
        hash2[thisletter] = 1
      end
    end
    print "letter count 1 #{lettercount1}\n"
    print "letter count 2 #{lettercount2}\n"
    puts(hash1)
    puts(hash2)
    hash1.keys.each do |thisletter|
      if hash2[thisletter]
        undercount = hash2[thisletter] - hash1[thisletter]
        if undercount > 0
          puts "Undercount #{thisletter} #{undercount}"
        end
      else
        puts "#{thisletter} is in hash1 but not in hash2"
      end
    end
    hash2.keys.each do |thisletter|
      if hash1[thisletter]
        overcount = hash1[thisletter] - hash2[thisletter]
        if overcount > 0
          puts "Overcount #{thisletter} #{overcount}"
        end
      else
        puts "#{thisletter} is in hash2 but not in hash1"
      end
    end
  end
  line_no += 1
end

