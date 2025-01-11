def get_formatted_name(first,last,middle=""):
   """Generate a neslty formatted full name"""
   if middle:
      fullname = first +" " + middle + " " + last
   else:
      fullname = first + " " + last
      
   return fullname.title();

