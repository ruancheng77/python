package #{package}.service;

import java.util.List;

import #{package}.pojo.#{object};

import com.github.pagehelper.Page;


public interface I#{object}Service {

	int save(#{object} record);

	int remove(#{object} record);

	int updateByPrimaryKey(#{object} record);

	int countAllRecord();

	#{object} getByPrimaryKey(Object key);

	List<#{object}> listAll();

	List<#{object}> listByPage(Page<#{object}> page);
}
