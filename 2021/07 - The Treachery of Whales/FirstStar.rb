require_relative 'CrabOrganiser'

crabs = CrabOrganiser.new(File.read('./TestCase.txt'))
p crabs.travel
