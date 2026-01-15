# Test Case 8: Verify All Products and product detail page
def test_all_products_and_product_detail(homepage):
    # 4. Click on 'Products' button
    product_page = homepage.header.click_products_button()
    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    product_page.is_all_products_page()
    # 6. The products list is visible
    product_page.product_list.is_product_list_visible()
    # 7. Click on 'View Product' of first product
    product_detail_page = product_page.product_list.click_view_nth_product(0)
    # 8. User is landed to product detail page
    # 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
    product_detail_page.is_product_detail_visible()

# Test Case 9: Search Product
def test_search_product(homepage):
    # 4. Click on 'Products' button
    product_page = homepage.header.click_products_button()
    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    product_page.is_all_products_page()
    # 6. Enter product name in search input and click search button
    keyword = "Top"
    product_page.search_product(keyword)
    # 7. Verify 'SEARCHED PRODUCTS' is visible
    product_page.is_searched_product_visible()
    # 8. Verify all the products related to search are visible
    product_page.product_list.is_product_list_visible()

# Test Case 18: View Category Products
def test_view_category_products(homepage):
    # 3. Verify that categories are visible on left side bar
    homepage.category_list.is_category_list_visible()
    # 4. Click on 'Women' category
    homepage.category_list.click_category("Women")
    # 5. Click on any category link under 'Women' category, for example: Dress
    subcategory = homepage.category_list.get_nth_subcategory("Women", 0)
    product_page = homepage.category_list.click_nth_subcategory("Women", 0)
    # 6. Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'
    product_page.product_list.verify_product_list_title(f"WOMEN - {subcategory.upper()} PRODUCTS")
    # 7. On left side bar, click on any sub-category link of 'Men' category
    product_page.category_list.click_category("Men")
    subcategory = product_page.category_list.get_nth_subcategory("Men", 0)
    product_page = product_page.category_list.click_nth_subcategory("Men", 0)
    # 8. Verify that user is navigated to that category page
    product_page.product_list.verify_product_list_title(f"MEN - {subcategory.upper()} PRODUCTS")

# Test Case 19: View Brand Products
def test_view_brand_products(homepage):
    # 4. Verify that Brands are visible on left side bar
    homepage.brand_list.is_brand_list_visible()
    # 5. Click on any brand name
    product_page = homepage.brand_list.click_brand("POLO")
    # 6. Verify that user is navigated to brand page and brand products are displayed
    product_page.product_list.verify_product_list_title("BRAND - POLO PRODUCTS")
    product_page.product_list.is_product_list_visible()
    # 7. On left side bar, click on any other brand link
    product_page = product_page.brand_list.click_brand("H&M")
    # 8. Verify that user is navigated to that brand page and can see products
    product_page.product_list.verify_product_list_title("BRAND - H&M PRODUCTS")
    product_page.product_list.is_product_list_visible()