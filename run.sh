echo "------------------------------------"
echo "Part I"
echo "------------------------------------"
cd part_one

echo "Executing main"
echo "------------------------------------"
python main.py
echo " "

cd tests
echo "------------------------------------"
echo "Executing positive unit tests:"
echo "------------------------------------"
echo " "
python -m unittest -v positive_tests

echo "------------------------------------"
echo "Executing negative unit tests"
echo "------------------------------------"
echo " "
python -m unittest -v positive_tests
cd ..
cd ..

echo " "
echo "------------------------------------"
echo "Part II"
echo "------------------------------------"
cd part_two
echo "Running automation with Chrome in headless mode"
echo "------------------------------------"
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py -hl True
echo " "

echo "------------------------------------"
echo "Running automation with Firefox and not in headless mode"
echo "------------------------------------"
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py --browser FIREFOX -hl False
echo " "

echo "------------------------------------"
echo "Thanks"
echo "------------------------------------"
