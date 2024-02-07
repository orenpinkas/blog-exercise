#!/bin/zsh

# Check if the first argument is a number (integer)
if [[ $1 =~ ^-?[0-9]+$ ]]; then
  # If it's a number, check if it's lte 10000
  if (( $1 <= 10000 )); then
    echo "Re-seeding the database with $1 posts..."
  else
    echo "Error: $1 is too big." >&2
    exit 1
  fi
else
  echo "Error: $1 is not a number." >&2
  exit 1
fi

# drop db
python manage.py sqlflush | python manage.py dbshell

echo "db dropped!"

# seed
python manage.py seed $1

echo "db seeded.."

# create superuser
python ./create_superuser.py

echo "done!"